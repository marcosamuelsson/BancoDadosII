/*Select mais otimizado*/
SELECT name, 'domain', industry, locality FROM companies_sorted WHERE industry = 'military' LIMIT 200;