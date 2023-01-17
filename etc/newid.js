/*
신규 아이디 추천
https://programmers.co.kr/learn/courses/30/lessons/72410
아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
*/
function solution(new_id) {
    let answer = '';
    
    answer = new_id.toLowerCase() // 소문자
                .replace(/[^\w-_.]/g, '') // 비허용 문자 제거
                .replace(/\.{2,}/g, '.').replace(/^\./g, '').replace(/\.$/g, '') // 마침표 제거
                .substring(0, 15) // 3~15자
                .replace(/^\./g, '').replace(/\.$/g, ''); // 마침표 제거

    const len = answer.length;

    if(len == 0) {
        return 'aaa';
    }

    if(len < 3) {
        const lastStr = answer.substr(-1);
        answer = answer + lastStr.repeat(3 - len);
    }

    return answer;
}



function solution(new_id) {
    const answer = new_id
        .toLowerCase() // 1
        .replace(/[^\w-_.]/g, '') // 2
        .replace(/\.+/g, '.') // 3
        .replace(/^\.|\.$/g, '') // 4
        .replace(/^$/, 'a') // 5
        .slice(0, 15).replace(/\.$/, ''); // 6
    const len = answer.length;
    return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}
