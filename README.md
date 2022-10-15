class_ml_lab1
==============================


## Требования к реализации

* Нужно выбрать метрику качества и обосновать ее выбор (1 балл).

* Нужно написать стадии для полного цикла жизни ML модели (4 баллов)
    1. **Препроцессинг.**
    1. **Разделение данных train/val**
    1. **Генерация признаков.** Обратите внимание, что если вы генерируете признаки, которые предполагают обучение на тренировочном датасете (fit), то для валидационного вы должны применять уже обученные трансормации (transform). Так, если бы данные из val к вам пришли из будущего и у вас нет для них правильных ответов. **Данные из val вы никак не используете в обучении/тюнинге параметров/и т.д., только для оценки качества.** Представьте, что данных val у Вас на момент создания модели нет, они придут к вам только в будущем.
    1. **Обучение модели.**
        * Здесь вы можете использовать внутри различные методы оценки качества модели train/test split, k-fold validation и т.д. [Многие из них уже реализованы в scikit-learn](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection). Вы их используете "для себя" чтобы решить какую модель/ модели вы отправите дальше работать с "реальным миром".
        * Нужно имплементировать
            1. Что-то из scikit-learn используя [Scikit-Learn Pipelines...](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.pipeline)
            1. [Catboost](https://catboost.ai)
            1. Если захочется, то что-то еще. Больше - можно, меньше - нет.
    1. **Оценка модели** по метрике качества, выбранном в первом пункте на val датасете и [сохранение метрик / графиков](https://dvc.org/doc/start/data-management/metrics-parameters-plots).
    1. **Предсказание (инференс) модели на новых данных.**
    
* Из стейджей выше соберите **один или два пайплайна** (1 балл):
    1. Обучения модели и ее оценки
    1. Инференса модели

* В пайплайнах используется работа с категориальными признаками (2 балла):
    * [CategoricalEncoders](https://contrib.scikit-learn.org/category_encoders/targetencoder.html)
    * [Тюнинг параметров отвечающих за работу с категориями Catboost](https://github.com/catboost/tutorials/blob/master/categorical_features/categorical_features_parameters.ipynb)
* Для [управления данными](https://dvc.org/doc/start/data-management) и [экспериментами](https://dvc.org/doc/start/experiment-management/experiments) использован DVC (2 балла).

Код должен быть написан в функциях и разнесен по модулям шаблона. Если вы изменяете шаблон - напишите об этом комментарий, какая мотивация.
Вы можете использовать ноутбук для разработки, но нужно писать код так, чтобы это потом было легко перенести в функции и разнести по модулям проекта. Пример такой работы мы разбирали на [практике](https://eduhseru.sharepoint.com/:v:/s/AdvancedDataAnalysis2022/EZw_TeFlH5tGgiDp_LO-8JkByc1kg24mZVN9Y4c42MRuPQ?e=f7aCbE).


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
