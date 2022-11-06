/Applications/Virtuoso\ Open\ Source\ Edition\ v7.2.app/Contents/virtuoso-opensource/bin/isql \
exec="ld_dir ('/Users/xuyou/Downloads/berlin-sparql-benchmark/Virtuoso/data', '*.ttl', 'berlin_1'); \
rdf_loader_run(); \
rdf_load_stop();"