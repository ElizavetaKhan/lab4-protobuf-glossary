from typing import Dict

try:
    from app.src.models import Entry
except ImportError:
    from .models import Entry

glossary: Dict[str, Entry] = {
    "usability_test": Entry(
        name="usability_test",
        description="метод оценки удобства использования интерфейса путем наблюдения за реальными пользователями.",
        reference="https://ru.wikipedia.org/wiki/Юзабилити-тестирование"
    ),
    "heuristic_evaluation": Entry(
        name="heuristic_evaluation",
        description="экспертный анализ интерфейса по набору правил или принципов (эвристик).",
        reference="https://dsgners.ru/bikbye/3136-evristicheskaya-otsenka-moschnyiy-ux-instrument-v-rukah-dizaynera"
    ),
    "a_b_testing": Entry(
        name="a_b_testing",
        description="метод сравнения двух версий интерфейса, чтобы определить, какая лучше выполняет задачу пользователя.",
        reference="https://ru.wikipedia.org/wiki/A/B-тестирование"
    ),
}