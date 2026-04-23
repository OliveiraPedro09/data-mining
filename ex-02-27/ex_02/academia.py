import pandas as pd

# =========================
# TABELA CURSOS
# =========================
df_cursos = pd.DataFrame({
    'id_curso': [1, 2, 3],
    'nome_curso': ['Administração', 'Engenharia', 'Sistemas de Informação']
})

# =========================
# TABELA DISCIPLINAS
# =========================
df_disciplinas = pd.DataFrame({
    'id_disciplina': [101, 102, 103, 104, 105],
    'nome_disciplina': ['Matemática', 'Programação', 'Física', 'Banco de Dados', 'Gestão'],
    'id_curso': [2, 3, 2, 3, 1]
})

# =========================
# TABELA PROFESSORES
# =========================
df_professores = pd.DataFrame({
    'id_professor': [201, 202, 203],
    'nome_professor': ['Carlos Silva', 'Ana Souza', 'Marcos Lima']
})

# =========================
# TABELA ALUNOS
# =========================
df_alunos = pd.DataFrame({
    'id_aluno': [301, 302, 303, 304, 305, 306],
    'nome_aluno': ['João', 'Maria', 'Pedro', 'Lucas', 'Juliana', 'Fernanda'],
    'id_curso': [1, 2, 3, 3, 2, 1]
})

# =========================
# TABELA MATRÍCULAS (TABELA CENTRAL)
# =========================
df_matriculas = pd.DataFrame({
    'id_matricula': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    'id_aluno': [301, 302, 303, 304, 305, 306, 301],
    'id_disciplina': [105, 101, 102, 104, 103, 105, 101],
    'id_professor': [203, 201, 202, 202, 201, 203, 201]
})

print(df_cursos)
print(df_disciplinas)
print(df_professores)
print(df_alunos)
print(df_matriculas)
