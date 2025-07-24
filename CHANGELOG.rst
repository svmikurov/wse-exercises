0.4.2 (24-07-2025)
==================

- Added `NumberAnswer` model
- Added `CheckResponse` model
- Added `SimpleCalcAnswer` model for simple calculation math task answer
- Added `SimpleCalcResult` model for answer checking result

- Added `ttl` field to `Config` model
- Added `time` field to `SimpleCalcConditions` model
- Added `checked_at` field to `CheckResponse` model
- Added `is_rewardable` field to `HandleAnswer` model
- Added `is_rewardable` field to `TaskRequest` model
- Updated `str` to `uuid.UUID` 'uid' field type in `CheckRequest`
- Updated `str` to `uuid.UUID` 'uid' field type in `TaskResponse`

- Renamed `MathExercise` enumeration to `MathEnum`
- Renamed `Exercise` enumeration to `ExerciseEnum`
- Renamed `HandleAnswer` model to `CheckRequest`
- Renamed `SimpleCalcHandle` model to `SimpleCalcAnswer`

- Added serialization and deserialization of the UUID type field to the `ConvertMixin` methods.
- Added `ConversionError` the base exception for all conversion-related errors
- Added error raising to `ConvertMixin` for instantiate methods

Typing
- Added `types.py` module with types
- Added type vars import from root package
- Added type vars: 'TaskT', 'TaskT_co', 'TaskT_contr', 'AnswerT', 'ConditionsT',
  'ConfigT', 'ExerciseT', 'QuestionT',

0.4.0 (08-07-2025)
==================

- Added `ConvertMixin` and `BaseShema`
- Added exercise type mapping `MATH_EXERCISES`
- Renamed classes
- Rename `mathem` package to `math`
- Update imports

0.3.3 (01-07-2025)
==================

- Renamed `ISimpleMathExercise` to `ISimpleCalcTask`

0.3.2 (01-07-2025)
==================

- Renamed `ISimpleMathExercise` to `ISimpleMathTask`
- Updated type Task dependencies
- Added base classes for Task components

0.3.1 (30-06-2025)
==================

- Updated `pydantic` methods.
- Updated tests.

0.3.0 (30-06-2025)
==================

- Downgraded `pydantic` version to 1.10.22.

0.1.2 (29-05-2025)
==================

- The library is marked as typed for third-party type checking.
- Updated typing.
- Refactor mathematical simple calculations.

0.1.1 (20-05-2025)
==================

- Added tests.
- Removed interface protocols.
- Improved annotations.
- Added `pydantic` models.
- Added task factories.

0.1.0 (19-05-2025)
==================

- Initial published version.