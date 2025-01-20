#!/bin/bash

# 스크립트 실행 중 오류 발생 시 중단
set -e

# 현재 폴더 이름 저장
current_dir=$(basename "$PWD")

# 날짜 정보 가져오기 (월, 일)
month=$(date +"%m")
day=$(date +"%d")

# Git 저장소의 루트 디렉토리로 이동
# 필요 시 아래 경로를 실제 Git 저장소의 경로로 변경하세요.
# 예: 
cd C\SSAFY || { echo "Git 저장소로 이동 실패"; exit 1; }

# 제출 폴더가 Git 저장소에 있는지 확인
if [ ! -d "$current_dir" ]; then
    echo "현재 폴더가 Git 저장소의 하위 폴더가 아닙니다."
    exit 1
fi

# 제출 폴더로 이동
cd "$current_dir"

# 이전 커밋에서 오늘 날짜에 해당하는 커밋 수를 세어 수정 횟수 계산
revision=$(git log --grep="과제 제출 ${month}월 ${day}일" --pretty=oneline | wc -l)

if [ "$revision" -eq 0 ]; then
    revision_msg="0차"
else
    revision_msg="${revision}차"
fi

# 커밋 메시지 생성
commit_message="과제 제출 ${month}월 ${day}일/${revision_msg} 수정"

echo "커밋 메시지: $commit_message"

# 변경된 모든 파일을 스테이징
git add .

# 커밋
git commit -m "$commit_message"

# 원격 저장소에 푸시
git push

# 상위 디렉토리로 이동
cd ..

# 제출 폴더 삭제
rm -rf "$current_dir"

echo "과제가 성공적으로 제출되고 폴더가 삭제되었습니다."
