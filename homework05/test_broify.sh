#!/bin/sh

WORKSPACE=/tmp/broify.$(id -u)

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

cat > $WORKSPACE/input0 <<EOF
# Super useful comment describing a tricky configuration option
SETUP_THE_BOMB="no" # Hide the evidence

# Another super userful comment
BASE_OWNERSHIP="us" # All your base are belong to...
EOF

cat > $WORKSPACE/output0 <<EOF
SETUP_THE_BOMB="no"
BASE_OWNERSHIP="us"
EOF

cat > $WORKSPACE/output0W <<EOF

SETUP_THE_BOMB="no"


BASE_OWNERSHIP="us"
EOF

cat > $WORKSPACE/input1 <<EOF
// C++ is so cool
int main() {
    // Totes
    return 0;	// YESSS
}
EOF

cat > $WORKSPACE/output1 <<EOF
int main() {
    return 0;
}
EOF

cat > $WORKSPACE/output1W <<EOF

int main() {

    return 0;
}
EOF


./broify.sh < $WORKSPACE/input0 | diff -y - $WORKSPACE/output0 > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed BASE Test"
fi

./broify.sh -W < $WORKSPACE/input0 | diff -y - $WORKSPACE/output0W > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed BASE Test (-W)"
fi

./broify.sh -d '//' < $WORKSPACE/input1 | diff -y - $WORKSPACE/output1 > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed C++ Test"
fi

./broify.sh -d '//' -W < $WORKSPACE/input1 | diff -y - $WORKSPACE/output1W > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed C++ Test (-W)"
fi

echo "broify.sh test succesful!"
exit 0
