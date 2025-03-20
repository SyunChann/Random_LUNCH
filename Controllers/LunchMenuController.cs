using Microsoft.AspNetCore.Mvc;
using OfficeOpenXml;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace YourNamespace.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class LunchMenuController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetLunchMenus()
        {
            // 엑셀 파일 경로 설정 (wwwroot 폴더에 있어야 합니다)
            string filePath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "서대문역 점심 메뉴.xlsx");

            if (!System.IO.File.Exists(filePath))
            {
                return NotFound("엑셀 파일을 찾을 수 없습니다.");
            }

            List<object> menus = new List<object>();

            // 엑셀 파일 읽기
            using (var package = new ExcelPackage(new FileInfo(filePath)))
            {
                var worksheet = package.Workbook.Worksheets.First();
                var rowCount = worksheet.Dimension.Rows;

                for (int row = 3; row <= rowCount; row++)
                {
                    menus.Add(new
                    {
                        순번 = worksheet.Cells[row, 1].Text,
                        종류 = worksheet.Cells[row, 2].Text,
                        상호명 = worksheet.Cells[row, 3].Text,
                        가격 = worksheet.Cells[row, 4].Text,
                        맛 = worksheet.Cells[row, 5].Text,
                        양 = worksheet.Cells[row, 6].Text,
                        위치 = worksheet.Cells[row, 7].Text,
                        추천메뉴 = worksheet.Cells[row, 8].Text
                    });
                }
            }

            return Ok(menus);
        }
    }
}