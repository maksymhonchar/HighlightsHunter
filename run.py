import datetime

from app.customthresholdcaserunner import CustomThresholdCaseRunner
from app.adaptivethresholdcaserunner import AdaptiveThresholdCaseRunner
from app.dogblobcaserunner import DogBlobCaseRunner


def main() -> None:
    runners = {
        'custom threshold algorithm': CustomThresholdCaseRunner,
        'adaptive threshold algorithm': AdaptiveThresholdCaseRunner,
        'DOG blob detector algorithm': DogBlobCaseRunner,
    }
    for case_title, case_runner_cls in runners.items():
        print(f'[DBG] [{datetime.datetime.now()}] start running case {case_title}')
        runner = case_runner_cls()
        runner.run(
            data_dir_path='data',
            output_dir_path='output',
            n_pixels=10
        )
        print(f'[DBG] [{datetime.datetime.now()}] end running case {case_title}')


if __name__ == '__main__':
    main()
