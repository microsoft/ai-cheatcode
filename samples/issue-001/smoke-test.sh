#!/bin/bash
# Smoke test for the PDF Agent deployment
# Run after `azd up` to verify the deployment is working
#
# Usage: ./smoke-test.sh <function-app-url> <function-key>

set -e

BASE_URL="${1:?Usage: ./smoke-test.sh <function-app-url> <function-key>}"
FUNC_KEY="${2:?Usage: ./smoke-test.sh <function-app-url> <function-key>}"

echo "=== PDF Agent Smoke Test ==="
echo "Target: $BASE_URL"
echo ""

# Test 1: Status endpoint
echo "1. Testing /api/status..."
STATUS=$(curl -s -w "\n%{http_code}" "$BASE_URL/api/status?code=$FUNC_KEY")
HTTP_CODE=$(echo "$STATUS" | tail -1)
BODY=$(echo "$STATUS" | head -1)

if [ "$HTTP_CODE" = "200" ]; then
    echo "   ✅ Status endpoint OK"
    echo "   Response: $BODY"
else
    echo "   ❌ Status endpoint failed (HTTP $HTTP_CODE)"
    echo "   Response: $BODY"
    exit 1
fi
echo ""

# Test 2: Query with no documents (should return helpful message)
echo "2. Testing /api/query with no documents..."
QUERY_RESULT=$(curl -s -w "\n%{http_code}" \
    -X POST "$BASE_URL/api/query?code=$FUNC_KEY" \
    -H "Content-Type: application/json" \
    -d '{"question": "What compliance requirements are mentioned?"}')
HTTP_CODE=$(echo "$QUERY_RESULT" | tail -1)
BODY=$(echo "$QUERY_RESULT" | head -1)

if [ "$HTTP_CODE" = "200" ]; then
    echo "   ✅ Query endpoint OK"
    echo "   Response: $BODY"
else
    echo "   ⚠️  Query returned HTTP $HTTP_CODE (may be expected if no docs uploaded)"
    echo "   Response: $BODY"
fi
echo ""

# Test 3: Upload a test PDF (if one exists in data/sample-pdfs/)
SAMPLE_PDF="data/sample-pdfs/$(ls data/sample-pdfs/*.pdf 2>/dev/null | head -1)"
if [ -f "$SAMPLE_PDF" ]; then
    echo "3. Testing /api/upload with $SAMPLE_PDF..."
    UPLOAD_RESULT=$(curl -s -w "\n%{http_code}" \
        -X POST "$BASE_URL/api/upload?code=$FUNC_KEY" \
        -F "file=@$SAMPLE_PDF")
    HTTP_CODE=$(echo "$UPLOAD_RESULT" | tail -1)
    BODY=$(echo "$UPLOAD_RESULT" | head -1)

    if [ "$HTTP_CODE" = "200" ]; then
        echo "   ✅ Upload endpoint OK"
        echo "   Response: $BODY"
    else
        echo "   ❌ Upload failed (HTTP $HTTP_CODE)"
        echo "   Response: $BODY"
    fi
else
    echo "3. ⏭️  Skipping upload test (no sample PDFs in data/sample-pdfs/)"
    echo "   Add a PDF and re-run, or upload manually via:"
    echo "   curl -X POST '$BASE_URL/api/upload?code=$FUNC_KEY' -F 'file=@your-doc.pdf'"
fi
echo ""

echo "=== Smoke test complete ==="
