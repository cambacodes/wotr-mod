using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;

namespace RanRomance.Tere;

public class TereEpil
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
		ActionsBuilder onShow = ActionsBuilder.New().MarkCuesSeen("RanRomTereSlide0001").MarkCuesSeen("RanRomTereSlide0002")
			.MarkCuesSeen("RanRomTereSlide0003")
			.MarkCuesSeen("RanRomTereSlide0005")
			.MarkCuesSeen("RanRomTereSlide0006")
			.MarkCuesSeen("RanRomTereSlide0007");
		BookPageConfigurator.For("RanRomTereSlide0001").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomTereSlide0002").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomTereSlide0003").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomTereSlide0005").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomTereSlide0006").SetOnShow(onShow).Configure();
		BookPageConfigurator.For("RanRomTereSlide0007").SetOnShow(onShow).Configure();
	}
}
