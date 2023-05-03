from transformers import T5Tokenizer, T5ForConditionalGeneration


class ChitChatGenerator:
    def __init__(self, ):
        self.chitchat_model = T5ForConditionalGeneration.from_pretrained(
            "madhavappaneni/t5-small-chit-chat", use_auth_token="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")
        self.chitchat_tokenizer = T5Tokenizer.from_pretrained(
            "madhavappaneni/t5-small-chit-chat", use_auth_token="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")

    def generate_response(self, input_text, context):
        input_ids = self.chitchat_tokenizer.encode(
            input_text, return_tensors='pt')
        outputs = self.chitchat_model.generate(
            input_ids, max_length=50)
        generated_text = self.chitchat_tokenizer.decode(
            outputs[0], skip_special_tokens=True)
        return generated_text
