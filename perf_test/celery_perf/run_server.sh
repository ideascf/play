#!/bin/bash
celery worker -A task -l INFO
