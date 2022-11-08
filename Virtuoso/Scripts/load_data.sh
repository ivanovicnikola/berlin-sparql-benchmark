/Applications/Virtuoso\ Open\ Source\ Edition\ v7.2.app/Contents/virtuoso-opensource/bin/isql \
exec="ld_dir ('/Users/xuyou/Downloads/berlin-sparql-benchmark/Virtuoso/data', '*.ttl', 'http://localhost:8890/berlin_1'); \
rdf_loader_run(); \
DELETE FROM DB.DBA.LOAD_LIST; \
rdf_load_stop(); \
checkpoint;"