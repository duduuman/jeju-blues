# -*- coding: utf-8 -*-
"""inference

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1enfCdlELRCd8w93kZtvlBiHFgERYmfoP
"""

def inference(sentence, model, tokenizer):
  model = MBartForConditionalGeneration.from_pretrained("/content/mnt/My Drive/translation/output_model/translation")
  tokenizer = tokenizer.from_pretrained('/content/mnt/My Drive/translation/output_model/translation')

  inputs = tokenizer(sentence, return_tensors="pt")
  translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["ko_KR"])
  translate = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)
  return translate