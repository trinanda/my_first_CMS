#!/usr/bin/env bash
alembic downgrade base
rm -rf migrasi_data/versions/*
alembic revision --autogenerate -m 'inisial database'
alembic upgrade head