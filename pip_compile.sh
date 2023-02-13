#!/bin/bash
pip-compile -U --resolver=backtracking --strip-extras requirements.in
pip-compile -U --resolver=backtracking --strip-extras requirements-test.in
pip-compile -U --resolver=backtracking requirements-dev.in
