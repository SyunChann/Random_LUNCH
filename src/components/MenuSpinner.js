import React, { useState, useEffect } from "react";
import axios from "axios";
import MenuResult from "./MenuResult";

const MenuSpinner = () => {
  const [menus, setMenus] = useState([]); // 메뉴 데이터를 저장
  const [selectedMenu, setSelectedMenu] = useState(null); // 선택된 메뉴

  useEffect(() => {
    fetchSheetData();
  }, []);

  const fetchSheetData = () => {
    const spreadsheetId = "1lMZplkWXUbBaZCiPwYDijHtctIO5Rgb-81F5QX3Tgqs"; // 스프레드시트 ID
    const range = "BR 런치!A4:J"; // 가져올 데이터 범위
    const apiKey = "구글 스프레드 API Key 추가"; // API 키 추가

    const url = `https://sheets.googleapis.com/v4/spreadsheets/${spreadsheetId}/values/${range}?key=${apiKey}`;

    axios
      .get(url)
      .then((response) => {
        console.log("📌 API 응답 데이터:", response.data.values); // 데이터 확인
        const rows = response.data.values;

        if (rows && rows.length > 0) {
          setMenus(
            rows.map((row) => ({
              순번: row[0] || "",
              종류: row[1] || "",
              상호명: row[2] || "",
              가격: row[3] || "",
              맛: row[4] || "",
              양: row[5] || "",
              위치: row[6] || "",
              "추천 메뉴": row[7] || "없음",
              특징: row[8] || "",
              네이버지도: row[9] || "#",
            }))
          );
        } else {
          console.warn("⚠️ 가져온 데이터가 없습니다.");
        }
      })
      .catch((error) => {
        console.error("❌ 스프레드시트 데이터를 가져오는 중 오류 발생:", error);
      });
  };

  const spin = () => {
    if (menus.length > 0) {
      const randomIndex = Math.floor(Math.random() * menus.length);
      console.log("🎯 선택된 인덱스:", randomIndex);
      console.log("🍽 선택된 메뉴:", menus[randomIndex]);
      setSelectedMenu(menus[randomIndex]);
    } else {
      console.warn("⚠️ 메뉴 데이터가 비어 있습니다!");
    }
  };

  return (
    <div className="container">
      <h1>서대문역 점심 메뉴 돌림판</h1>
      <MenuResult selectedMenu={selectedMenu} />
      <button onClick={spin} disabled={menus.length === 0}>돌려주세요!</button>
    </div>
  );
};

export default MenuSpinner;
