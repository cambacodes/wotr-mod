"""Auto-discovered harem row modules; each exposes register(payload, scenes, refs)."""
import importlib
import pkgutil
import copy


def register_all(payload, scenes, refs):
    from storylines import household, lastcall_ledger, lastcall_partners, foresight, harem_caps
    # Older row adapters use the authoring collectors. Drain those collectors
    # into this assembled payload and restore them, so builds stay isolated.
    collectors = (household.ENTRIES, household.INVITATIONS, lastcall_ledger.EXTRA_ENTRIES)
    snapshots = [copy.deepcopy(items) for items in collectors]
    partners = copy.deepcopy(lastcall_partners.PARTNERS)
    consumers = dict(household.CONSUMERS)
    foresight_consumers = dict(foresight.CONSUMERS)
    _body_seats(payload)
    try:
        for info in sorted(pkgutil.iter_modules(__path__), key=lambda m: m.name):
            if info.name.startswith('_'):
                continue
            _refresh_caps(payload)
            importlib.import_module(__name__ + "." + info.name).register(payload, scenes, refs)
            # A row may replace the list while retaining every existing scene.
            scenes = payload['Scenes']
            ids = {s['Id'] for s in scenes}
            for items in collectors[:2]:
                for body in items:
                    if body['Id'] not in ids:
                        scenes.append(copy.deepcopy(body))
                        ids.add(body['Id'])
            entries = payload['Books']['trickster.ledger']['Entries']
            ids = {entry['Id'] for entry in entries}
            entries.extend(copy.deepcopy(entry) for entry in collectors[2] if entry['Id'] not in ids)
            by_id = {body['Id']: body for body in scenes}
            for partner in lastcall_partners.PARTNERS:
                host = by_id.get(partner['key'] + '.lastcall.page')
                if host is None:
                    continue
                target = host['Nodes'][0].setdefault('Paragraphs', [])
                have = {paragraph['Text'] for paragraph in target}
                previous = next(p for p in partners if p['key'] == partner['key'])
                old = {paragraph['Text'] for paragraph in previous['paragraphs']}
                target.extend(copy.deepcopy(paragraph) for paragraph in partner['paragraphs']
                              if paragraph['Text'] not in have | old)
        pending = payload.setdefault('PendingHooks', [])
        pending[:] = list(dict.fromkeys(pending))
        payload['ForesightConsumers'] = {
            **payload.get('ForesightConsumers', {}), **foresight.CONSUMERS, **household.CONSUMERS}
        _refresh_caps(payload)
        harem_caps.apply(payload)
    finally:
        for items, snapshot in zip(collectors, snapshots):
            items[:] = snapshot
        household.CONSUMERS.clear()
        household.CONSUMERS.update(consumers)
        foresight.CONSUMERS.clear()
        foresight.CONSUMERS.update(foresight_consumers)
        lastcall_partners.PARTNERS[:] = partners


def _refresh_caps(payload):
    # Rebuild the existing limits against the final set of row witnesses.
    counts = payload.setdefault('Counts', {})
    for key in list(counts):
        if key.startswith('household.cap.'):
            del counts[key]


def _body_seats(payload):
    """S10's named seats read existing party bodies or current Drezen copies."""
    # Verified NenioInParty BlueprintEtude in /wrath/blueprints.zip.
    payload['Etudes']['nenio.in_party'] = '94503247ce3979a468c54a42a4b862bd'
    for woman in ('seelah', 'nenio'):
        key = 'household.pair.seelah_nenio.body.' + woman
        groups = [[woman + '.in_party']]
        for name, presence in payload['Presences'].items():
            if name not in (woman + '.presence', woman + '.presence.arcade'):
                continue
            local = key + '.' + name
            inputs = list(presence.get('Requires', []))
            for index, group in enumerate(presence.get('RequiresAnyGroups', [])):
                any_key = local + '.any.' + str(index)
                payload['Derived'][any_key] = [[flag] for flag in group]
                inputs.append(any_key)
            payload['Derived'][local] = [inputs]
            payload['DerivedForbids'][local] = list(dict.fromkeys([
                *presence.get('Forbids', []), name + '.failed', woman + '.epoch_unavailable']))
            groups.append([local])
        payload['Derived'][key] = groups
        route = payload['Relationships'][woman]
        losses = list(dict.fromkeys(route.get('UnavailableFlags', []) + route.get('EpochUnavailableFlags', [])))
        payload['SeatWomen'][woman] = dict(Relationship=woman, Requires=[woman + '.present_now', key],
            UnavailableFlags=losses, UnavailableOverrides=dict(route.get('UnavailableOverrides', {})))
