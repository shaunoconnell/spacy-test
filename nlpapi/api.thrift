namespace py spacy

struct EntityLabel {
    1: required string label;
    2: required i64 startCharOffset;
    3: required i64 endCharOffset;
}

struct LabeledEntities {
    1: required string text;
    2: required list<EntityLabel> labels;
}

struct EntitySpan {
    1: required string text;
    2: required string entityType;
    3: optional i32 startPos;
    4: optional i32 endPos;
}

exception UnsupportedLanguage {
    1: required string language;
}

service NERExtractor {
    list<EntitySpan> entities(1:string language, 2:string text) throws (1: UnsupportedLanguage unsupported),
}

service NERTrainer {
    void acceptLabel (1:LabeledEntities labels),
    void train(),
}

