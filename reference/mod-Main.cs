using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Anev;

public class Main
{
	public static void Configure()
	{
		AnevChpt03Dial001.Configure();
		AnevChpt05Dial001.Configure();
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("6ce0e47ee5b94576a60c607ec0fc063d", negate: true).AnswerSelected("30d8a3b6f8f949feaff81aa82d34486e");
		ActionsBuilder ifTrue = ActionsBuilder.New().StartDialog(null, "6ce0e47ee5b94576a60c607ec0fc063d");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().DialogSeen("aca6f74af98549fab00bb1f82fa24878", negate: true).AnswerSelected("464440f178d6483aaae28e5a350631be");
		ActionsBuilder ifTrue2 = ActionsBuilder.New().StartDialog(null, "aca6f74af98549fab00bb1f82fa24878");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().DialogSeen("c47ffdc9a62b40ac9648ce6006673cb8", negate: true).AnswerSelected("43ff233169e146a78e3218bb47615784");
		ActionsBuilder ifTrue3 = ActionsBuilder.New().StartDialog(null, "c47ffdc9a62b40ac9648ce6006673cb8");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().DialogSeen("2936ff4e6e234702b7f59b469b57feaa", negate: true).AnswerSelected("126b48d9dad94a5bbead2aedc0ec4aa6");
		ActionsBuilder ifTrue4 = ActionsBuilder.New().StartDialog(null, "2936ff4e6e234702b7f59b469b57feaa");
		ConditionsBuilder conditions5 = ConditionsBuilder.New().DialogSeen("2936ff4e6e234702b7f59b469b57feaa", negate: true).AnswerSelected("8de9e133dfed4ac9837f0004844c4647");
		ActionsBuilder ifTrue5 = ActionsBuilder.New().StartDialog(null, "2936ff4e6e234702b7f59b469b57feaa");
		ConditionsBuilder conditions6 = ConditionsBuilder.New().DialogSeen("9947a33fcd4543d18a6ab92ea292119f", negate: true).AnswerSelected("78301019d46a49e8b6f7fece0c9d1dda");
		ActionsBuilder ifTrue6 = ActionsBuilder.New().StartDialog(null, "9947a33fcd4543d18a6ab92ea292119f");
		ConditionsBuilder conditions7 = ConditionsBuilder.New().DialogSeen("ddcf04165a604410888aac8e752b1f92", negate: true).AnswerSelected("41a2ab2b568742fb9afe99ff8cd4f7e9");
		ActionsBuilder ifTrue7 = ActionsBuilder.New().StartDialog(null, "ddcf04165a604410888aac8e752b1f92");
		ConditionsBuilder conditions8 = ConditionsBuilder.New().DialogSeen("10aa555cd8d94da39977b09e0d848d77", negate: true).AnswerSelected("b7697dde817748e29c69c8ad606a6f9c");
		ActionsBuilder ifTrue8 = ActionsBuilder.New().StartDialog(null, "10aa555cd8d94da39977b09e0d848d77");
		ConditionsBuilder conditions9 = ConditionsBuilder.New().DialogSeen("1650593635d947f0b28fc1900b10d4d6", negate: true).AnswerSelected("865201b1d94d43e89244809005fe8eec");
		ActionsBuilder ifTrue9 = ActionsBuilder.New().StartDialog(null, "1650593635d947f0b28fc1900b10d4d6");
		ConditionsBuilder conditions10 = ConditionsBuilder.New().DialogSeen("91a3699b2b12496db23b33dad6746d31", negate: true).AnswerSelected("a19476e2956b4d428613a46470e11b7e");
		ActionsBuilder ifTrue10 = ActionsBuilder.New().StartDialog(null, "91a3699b2b12496db23b33dad6746d31");
		ConditionsBuilder conditions11 = ConditionsBuilder.New().DialogSeen("3b03b32bf11a431094a68776dc459065", negate: true).AnswerSelected("627ebab39cea4235a376d5fdf82eeae7");
		ActionsBuilder ifTrue11 = ActionsBuilder.New().StartDialog(null, "3b03b32bf11a431094a68776dc459065");
		ConditionsBuilder conditions12 = ConditionsBuilder.New().DialogSeen("32a15058781144dcb6bfcf440ab13236", negate: true).AnswerSelected("1c5b340c7fda462b9497f95466c734fc");
		ActionsBuilder ifTrue12 = ActionsBuilder.New().StartDialog(null, "32a15058781144dcb6bfcf440ab13236");
		ActionsBuilder finishActions = ActionsBuilder.New().Conditional(conditions, ifTrue).Conditional(conditions2, ifTrue2)
			.Conditional(conditions3, ifTrue3)
			.Conditional(conditions4, ifTrue4)
			.Conditional(conditions5, ifTrue5)
			.Conditional(conditions6, ifTrue6)
			.Conditional(conditions7, ifTrue7)
			.Conditional(conditions8, ifTrue8)
			.Conditional(conditions9, ifTrue9)
			.Conditional(conditions10, ifTrue10)
			.Conditional(conditions11, ifTrue11)
			.Conditional(conditions12, ifTrue12);
		DialogConfigurator.For("de4cc2dd71694b842be37b75d1705b83").SetFinishActions(finishActions).Configure();
		AnswersListConfigurator.For("33960c7f7af40cd43b7f801a76c87a0b").ClearAnswers().AddToAnswers("095eec5f820140de8259c8cdc4562de3")
			.AddToAnswers("207608856af1c4c42b83fc0d4891c9dc")
			.AddToAnswers("ac60b84ed62f25f42a2eb0b86e19d345")
			.AddToAnswers("c07e2266817155344bf23aa4e845cff9")
			.AddToAnswers("c13ae3f888a8ebb4e939fadd5d190f33")
			.AddToAnswers("bfea5c6073203754280d24c5947fc763")
			.AddToAnswers("085d2d94e3a8e754f9fd704d53119b04")
			.AddToAnswers("42fe1795525a613489febe886b9ab669")
			.AddToAnswers("786bd454321e347449f79473210e597e")
			.AddToAnswers("a30ea92d5e10c4b439329442e5e9d0b8")
			.AddToAnswers("9fdf3a04c1a9d614d88ec07d306afa84")
			.AddToAnswers("deaf7d362d1c8ad4190b75bea7409149")
			.AddToAnswers("57e13e1e51fe9254cab47a3f845b3707")
			.AddToAnswers("RanRomAnevChpt03Dial001Ans0001")
			.AddToAnswers("RanRomAnevChpt05Dial001Ans0001")
			.AddToAnswers("a2d96bffe3955594c9a87624d94fe81a")
			.AddToAnswers("7b8cf7b133641064aae60cdb468b40ab")
			.AddToAnswers("61590a9f2f8458c41a3ac2a9642cb091")
			.Configure();
	}
}
