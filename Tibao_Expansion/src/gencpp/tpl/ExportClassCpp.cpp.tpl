/****************************************************************************

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
****************************************************************************/

#include "${HEAD_FILE_NAME}.h"

${CLASS_HEAD_FILE_CONTENT}

static ${CLASS_NAME}* inst_${CLASS_NAME} = nullptr;

${CLASS_NAME}* ${CLASS_NAME}::share${CLASS_NAME}Inst() {
    if( !inst_${CLASS_NAME} ) {
        inst_${CLASS_NAME} = new ${CLASS_NAME}();
    }
    return inst_${CLASS_NAME};
} 

${CLASS_NAME}::${CLASS_NAME}() {
${MEMBER_INIT_CODE}
}

${CLASS_NAME}::~${CLASS_NAME}() {
${DELETE_MEMBER_CODE}
}

${MEMBER_FUNC_DEFINE}

