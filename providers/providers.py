from random import choice

from faker.providers import BaseProvider


roles = [
    'Desenvolvedor Back-end',
    'Desenvolvedor Front-end',
    'Gerente de Projetos',
    'Devops',
    'Tester',
    'Designer UX',
    'Designer UI',
    'DBA',
    'Scrum Master'
]


class Professions(BaseProvider):
    def role(self):
        return choice(roles)