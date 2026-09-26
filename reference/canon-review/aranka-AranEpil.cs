using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.DialogSystem.Blueprints;

namespace RanRomance.Aran;

public class AranEpil
{
	public static void Configure()
	{
		SlideAeon.Configure();
		Slide0001.Configure();
		Slide0002.Configure();
		Slide0004.Configure();
		Slide0005.Configure();
		SlideArue.Configure();
		SlideHulr.Configure();
		SlideChil.Configure();
		ConditionsBuilder conditionsBuilder = ConditionsBuilder.New().EtudeStatus(null, null, "4484a3460335465a992359fac23a2ca5", negate: false, null, true);
		ConditionsBuilder conditionsBuilder2 = ConditionsBuilder.New().EtudeStatus(null, null, "4484a3460335465a992359fac23a2ca5", negate: true, null, true);
		ConditionsBuilder conditionsBuilder3 = ConditionsBuilder.New().EtudeStatus(null, null, "6eddba9546e84c2fb0bb50af027b7d25", negate: false, null, true);
		ConditionsBuilder conditionsBuilder4 = ConditionsBuilder.New().EtudeStatus(null, null, "6eddba9546e84c2fb0bb50af027b7d25", negate: true, null, true);
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("265e41987fffe4a42ad67c667896a37a")).Conditions.Conditions[1] = conditionsBuilder.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("301e521b9050ba9459291e8028c5c852")).Conditions.Conditions[1] = conditionsBuilder2.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("d7673cb5225f3b44988e52866351b96e")).Conditions.Conditions[1] = conditionsBuilder.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("273ab429bf451204a824f372dddd3eac")).Conditions.Conditions[1] = conditionsBuilder.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("258991eb1b3e7974b93f3d96e76831dc")).Conditions.Conditions[0] = conditionsBuilder2.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("470d1082570f6bd459399d3f8f021a83")).Conditions.Conditions[1] = conditionsBuilder3.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("45b1938235d52f3449c55e89cdd3776d")).Conditions.Conditions[1] = conditionsBuilder3.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("d744a32aeb3e0804b98683deb56da799")).Conditions.Conditions[1] = conditionsBuilder3.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("4bb3706172f1ed54ca11db96254c4638")).Conditions.Conditions[1] = conditionsBuilder4.Build().Conditions[0];
		((BlueprintCueBase)BlueprintTool.Get<BlueprintCue>("8f6017d8d3bc5ec46b15773947e80c70")).Conditions.Conditions[0] = conditionsBuilder4.Build().Conditions[0];
		ActionsBuilder onShow = ActionsBuilder.New().MarkCuesSeen("RanRomAranSlide0001").MarkCuesSeen("RanRomAranSlide0002")
			.MarkCuesSeen("RanRomAranSlide0004")
			.MarkCuesSeen("RanRomAranSlide0005");
		BookPageConfigurator.For("RanRomAranSlide0001").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomAranSlide0002").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomAranSlide0004").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomAranSlide0005").SetOnShow(onShow).Configure();
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
