import React from "react";

const MenuResult = ({ selectedMenu }) => {
  if (!selectedMenu) return null;

  return (
    <div className="result">
      <h2>오늘의 메뉴는!</h2>
      <p><strong>종류</strong>: {selectedMenu.종류}</p>
      <p><strong>상호명</strong>: {selectedMenu.상호명}</p>
      <p><strong>가격</strong>: {selectedMenu.가격}</p>
      <p><strong>맛</strong>: {selectedMenu.맛}</p>
      <p><strong>양</strong>: {selectedMenu.양}</p>
      <p><strong>위치</strong>: {selectedMenu.위치}</p>
      <p><strong>추천 메뉴</strong>: {selectedMenu['추천 메뉴'] || '없음'}</p>
      <p><strong>특징</strong>: {selectedMenu.특징}</p>
      <p><strong>네이버 지도</strong>: <a href={selectedMenu.네이버지도} target="_blank" rel="noopener noreferrer">지도 보기</a></p>
    </div>
  );
};

export default MenuResult;
