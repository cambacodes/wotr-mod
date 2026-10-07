using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Mina;

public class MinaEpil
{
	public static void Configure()
	{
		SlideAeon.Configure();
		Slide0001.Configure();
		Slide0002.Configure();
		Slide0003.Configure();
		Slide0004.Configure();
		Slide0005.Configure();
		Slide0006.Configure();
		Slide0007.Configure();
		Slide0008.Configure();
		ActionsBuilder onShow = ActionsBuilder.New().MarkCuesSeen("RanRomMinaSlide0001").MarkCuesSeen("RanRomMinaSlide0002")
			.MarkCuesSeen("RanRomMinaSlide0003")
			.MarkCuesSeen("RanRomMinaSlide0004")
			.MarkCuesSeen("RanRomMinaSlide0005")
			.MarkCuesSeen("RanRomMinaSlide0006")
			.MarkCuesSeen("RanRomMinaSlide0007")
			.MarkCuesSeen("RanRomMinaSlide0008");
		BookPageConfigurator.For("RanRomMinaSlide0001").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomMinaSlide0002").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomMinaSlide0003").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomMinaSlide0004").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomMinaSlide0005").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomMinaSlide0006").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomMinaSlide0007").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomMinaSlide0008").SetOnShow(onShow).Configure();
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("91a3699b2b12496db23b33dad6746d31").AnswerSelected("b192e1e211654bcca27924c12e8aa617", null, negate: true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AddOrAndLogic(conditions, negate: true).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true);
		BookPageConfigurator.For("5c95d8e3fa4f3b44896914987cb04b0b").SetConditions(conditions2).Configure();
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
