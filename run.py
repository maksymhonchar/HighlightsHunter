import datetime
from typing import Dict

from app.customthresholdcaserunner import CustomThresholdCaseRunner


def main():
    runners: Dict[str, object] = {
        'custom threshold algorithm': CustomThresholdCaseRunner
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
