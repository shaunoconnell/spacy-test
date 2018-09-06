namespace py nlp.spacy

struct EntitySpan {
  1: required string text
  2: required string entityType
  3: optional i32 startPos
  4: optional i32 endPos
}

service NLP {
  list<EntitySpan> entities(1:string text)
}