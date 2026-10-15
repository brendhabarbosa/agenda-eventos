# agenda-eventos
Repositório para atividade de revisão para a prova da primeira etapa da disciplina de Desenvolvimento de Sistemas Web.

## Tentativa de excluir um local com eventos
Aparece a mensagem "Deleting the Local “PF” would require deleting the following protected related objects:
Evento: ETAL
Evento: Expotec
Evento: Julho das Pretas
Evento: Férias acadêmicas
" 
Isso ocorreu porque o on_delete é PROTECT, ou seja, ele garante que o o objeto não pode ser excluído a menos que os objetos associados também sejam.