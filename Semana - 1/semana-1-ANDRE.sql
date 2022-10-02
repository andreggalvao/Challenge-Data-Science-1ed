SELECT * FROM dados_mutuarios;
SELECT * FROM ids;
SELECT * FROM historicos_banco;
SELECT * FROM emprestimos;


SELECT * FROM ids A
LEFT JOIN dados_mutuarios B ON a.person_id = b.person_id
LEFT JOIN emprestimos C ON a.loan_id = c.loan_id
LEFT JOIN historicos_banco D on a.cb_id = d.cb_id