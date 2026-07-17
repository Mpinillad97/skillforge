## USER
id
email
password_hash
created_at

## PROFILE
id
user_id
name
title
summary
experience_years

## SKILL
id
name
category

## USERSKILL
user_id
skill_id
level

## JOB
id
user_id
company
title
description
url
created_at

## JOB SKILL
job_id
skill_id
required_level

## ANALYSIS
id
job_id
match_score
missing_skills
recommendations
created_at

## FLOW
Usuario

↓

Guarda perfil

↓

Pega vacante

↓

Analizamos

↓

Generamos Match