#!/bin/bash

# 스크립트 실행 중 오류 발생 시 중단
set -e

# 날짜 정보 가져오기 (월, 일)
month=$(date +"%m")
day=$(date +"%d")

# Git 저장소의 루트 디렉토리 찾기
git_root=$(git rev-parse --show-toplevel 2>/dev/null || echo "")

# Git 저장소가 아니면 종료
if [ -z "$git_root" ]; then
    echo "현재 폴더가 Git 저장소의 하위 폴더가 아닙니다."
    exit 1
fi

# 현재 디렉토리를 Git 저장소 루트 기준 상대 경로로 변환
current_dir=$(git rev-parse --show-prefix)

# Git 저장소 내부인지 확인
if [ -z "$current_dir" ]; then
    echo "현재 폴더가 Git 저장소의 하위 폴더가 아닙니다. (올바른 상대 경로 없음)"
    exit 1
fi

# 디버깅용 출력 (필요 시 주석 해제)
echo "현재 폴더: $(pwd)"
echo "Git 루트: $git_root"
echo "상대 경로: $current_dir"

# 변경된 파일 추가
git add .

# 오늘 날짜의 커밋 횟수 계산
revision=$(git log --grep="과제 제출 ${month}월 ${day}일" --pretty=oneline | wc -l)

if [ "$revision" -eq 0 ]; then
    revision_msg="0차"
else
    revision_msg="${revision}차"
fi

# 커밋 메시지 생성
commit_message="과제 제출 ${month}월 ${day}일/${revision_msg} 수정"

echo "커밋 메시지: $commit_message"

# 커밋
git commit -m "$commit_message"

# 원격 저장소로 푸시
git push

# 현재 디렉토리 삭제
cd "$git_root"
rm -rf "$current_dir"

echo "과제가 성공적으로 제출되고 폴더가 삭제되었습니다."
