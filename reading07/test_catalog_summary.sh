#!/bin/sh

WORKSPACE=/tmp/catalog_summary.$(id -u)
URL=http://www3.nd.edu/~pbui/teaching/cse.20189.sp16/static/txt/test_catalog_summary.txt

error() {
    echo 1>&2 "ERROR: $@"
    [ -r $WORKSPACE/test ] && cat $WORKSPACE/test
    exit 1
}

cleanup() {
    rm -fr $WORKSPACE
    exit $1
}

mkdir $WORKSPACE

trap "cleanup 0" EXIT
trap "cleanup 1" INT TERM

cat > $WORKSPACE/output <<EOF
Total CPUs: 6330
Total Machines: 457
Most Prolific Type: bobbit
EOF

./catalog_summary.sh $URL | sed 's/^[[:space:]]*//g' | diff -y - $WORKSPACE/output > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed $URL test"
fi

echo "catalog_summary.sh test succesful!"
exit 0
