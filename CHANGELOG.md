<!-- insertion marker -->
<a name="0.1.0"></a>

## [0.1.0](https://github.com///compare/d270d12481f8b1d9ac2840b2ade2ea498a3f2168...0.1.0) (2025-03-01)

### Features

- add the torch dictionary ([6767c8a](https://github.com///commit/6767c8ab86a9c5bc9b28b008c2c6760e8071e46c))
- add tqdm dependency for progress tracking in data processing ([4b70499](https://github.com///commit/4b7049992896639906f3eae2fbec2006795076dd))
- add Word2Sequence class for word indexing and transformation ([1f7832e](https://github.com///commit/1f7832e4186c686163f3daede05fa89f6296091d))
- add IMDBEmbedding class for dataset embedding and processing ([1bc8135](https://github.com///commit/1bc81355e7a522972f78301da4067bdfb4a17397))
- update main.py to enhance dataset processing with random selection and improved data loading ([198331e](https://github.com///commit/198331e19c391d06a3250839e0be4beccd874b3f))
- add IMDBDataset and IMDBDataLoader classes for dataset management ([bc9aa18](https://github.com///commit/bc9aa186d97cb9422e13810bac6ddcf1068c3c48))
- enhance tokenizer and add paths_getter for improved data handling ([875a922](https://github.com///commit/875a92257e51406bdc203806edc0c70f86e295f0))
- update main.py to integrate paths_getter and tokenizer for dataset processing ([b8e8b03](https://github.com///commit/b8e8b033c5e08d85c109ab1d5099736af70045c4))
- add contraction mapping for common English contractions ([74e6b58](https://github.com///commit/74e6b58df12267843335ead8c9e5ca305761b604))
- add .gitignore to exclude __pycache__ directories ([72aea2b](https://github.com///commit/72aea2b44a0f40f68fd9895406cc93843e91d8b4))
- add Seed class for reproducibility and update __getitem__ method for test category ([973b9d4](https://github.com///commit/973b9d46a7eec3f745146481326cbcee8de01b71))
- implement IMDBDataset class for dataset handling and add tokenizer and labels_getter functions ([ef2f8e5](https://github.com///commit/ef2f8e5a90174f124635322ebd20d05beb62492e))
- integrate IMDBDataset for dataset handling in main.py ([bcbc028](https://github.com///commit/bcbc0284baec1dcddd25e813cb57172e899c707d))
- add torch dependency to requirements.txt ([fb66f1a](https://github.com///commit/fb66f1a8d7622bd72f591ac5991de01c498658fa))
- add new movie review files with diverse opinions and ratings ([14e03b9](https://github.com///commit/14e03b9e1bb2643da18059c1996f12967d553e56))
- add tokenizer function and labels getter to process text and retrieve labels ([d27293f](https://github.com///commit/d27293f44c0de417b68132aba7fc299db201a1e7))
- add tokenizer functionality to process movie review text ([98aca75](https://github.com///commit/98aca75fa10cbff592f752e241faa10d4b188f8d))
- add Timer class in tools.py for measuring elapsed time ([cd86bd9](https://github.com///commit/cd86bd9d6a2a51fc3c06861eb573e19c779a50ce))
- add models.py with Opener class for OpenAI API integration ([751c309](https://github.com///commit/751c309cbf727871b9b344c43b0d6bde0c6ff470))
- add __init__.py with main function and initial setup ([ae0f0e9](https://github.com///commit/ae0f0e96c271203efe98e5afdb8fb125b8be9d9d))
- add main.py with initial implementation and sentiment analysis reference ([6bfa883](https://github.com///commit/6bfa8833efd26bd7451080f077f30929c4306bef))

### Bug Fixes

- update __exit__ method signature in Timer class for proper exception handling ([bf984aa](https://github.com///commit/bf984aa2626832e1e1bfca54bb90e156117ceb60))

### Chore

- update .gitignore to exclude .DS_Store files ([4b3ad06](https://github.com///commit/4b3ad06317175204ff814b4e0d94843e6c2032a6))
- add .gitignore to exclude .DS_Store files ([ad8871f](https://github.com///commit/ad8871fd628d59368adec221072bde78965d1654))
- delete data files ([3a09b69](https://github.com///commit/3a09b694a044fd76baefde588a8d15e2dc7ef8c6))
- add pyproject.toml for changelog configuration ([925518d](https://github.com///commit/925518dd69e036be778ae4a8f7343f6e643b3499))

### Docs

- update CHANGELOG.md to reflect recent feature enhancements and corrections ([7e3737a](https://github.com///commit/7e3737aae9752072aa73662c77bd03c2dd183402))
- update CHANGELOG.md to include recent feature enhancements and corrections ([8eeb0a1](https://github.com///commit/8eeb0a1844fe1b81fad436d5fb15b0947acaa31f))
- update CHANGELOG.md to reflect recent feature additions and updates ([97e5f21](https://github.com///commit/97e5f2157a219cc74fba33c0e63de18ca138d59b))
- update CHANGELOG.md to include addition of Seed class and updates to __getitem__ method ([f2772dd](https://github.com///commit/f2772ddcf22079686f49388ccc2450f89f455fb8))
- update CHANGELOG.md to include recent feature additions for IMDBDataset class and integration ([8f6933c](https://github.com///commit/8f6933cb762c96958aca716dcec0c6834672449d))
- update CHANGELOG.md for version 0.1.0 release date correction ([ab6181c](https://github.com///commit/ab6181c653649cc8873cfbedf93c910142064086))
- update CHANGELOG.md to include recent feature additions ([2ea4bd6](https://github.com///commit/2ea4bd64e3d2471c179599c67b314df106d3a391))
- update README.md for improved dataset citation formatting ([185382d](https://github.com///commit/185382d68e246fbbb89f4748396a388e1a28bcb4))
- update CHANGELOG.md to categorize recent bug fixes and feature additions ([4765ba1](https://github.com///commit/4765ba193641d4394eb5a57d3775d2aba3c3623e))
- add CHANGELOG.md for version 0.1.0 with initial project features and updates ([9476b62](https://github.com///commit/9476b62677f22f1e0fe2d5ee999d08cae595f263))
- add README file with project introduction and dataset acknowledgment ([8e5ee51](https://github.com///commit/8e5ee511b030737d6d4b1bc9d7235cc272ee74b1))

### Code Refactoring

- update main.py to improve dataset processing and batch handling ([43f9043](https://github.com///commit/43f90438eb44afa08349da7130f62ea5e778f912))
- remove IMDBDataset and IMDBDataLoader classes to streamline dataset management ([8f7d5ed](https://github.com///commit/8f7d5ed11401e80fb53b148a42e28a192e1c4886))

### Dependencies

- add requirements file with project dependencies ([dc54a8b](https://github.com///commit/dc54a8b7d3ae27201f0975940423f19b4285b01e))

