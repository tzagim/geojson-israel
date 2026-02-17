# geojson-israel

גבולות היישובים במדינת ישראל (גבולות שיפוט סטטוטוריים) 
The borders of settlements in the State of Israel from the Ministry of the Interior

## מקור הנתונים
הנתונים נלקחו ישירות ממאגר הנתונים הפתוח של **משרד הפנים** (אגף מדידות ומפות / מערך הגיאו-אינפורמציה) דרך פלטפורמת ArcGIS Open Data.

- **שכבה מקורית**: גבולות שיפוט – יישובים / ועדים מקומיים  
- **קישור למקור**: [https://gvulot-shiput-statutory-moinil.opendata.arcgis.com/](https://gvulot-shiput-statutory-moinil.opendata.arcgis.com/)  
- **קובץ Shapefile מקורי**: [muni_vaadim](https://gisdata-moinil.opendata.arcgis.com/datasets/069298e81f8e4e6fb96aa59913c113cd)  
- **תאריך עדכון אחרון (בזמן יצירת הפרויקט)**: אוקטובר 2025

## מה יש כאן?
- כל יישוב/רשות מקומית/ועד מקומי בקובץ GeoJSON **נפרד**
- שם התיקייה ושם הקובץ מבוססים על השם באנגלית (`Muni_Eng`)
- הקואורדינטות הומרו מרשת ישראל החדשה (ITM / EPSG:2039) → **WGS84** (EPSG:4326)

## שדות properties
```json
"Muni_Heb"       // שם בעברית
"Muni_Eng"       // שם באנגלית
"Sug_Muni"       // סוג הרשות (מועצה מקומית / עירייה / מועצה אזורית ...)
"CR_PNIM"        // קוד פנימי משרד הפנים
"CR_LAMAS"       // קוד הלמ"ס
"Vaad_Heb"       // שם ועד מקומי (עברית)
"Vaad_Eng"       // שם ועד מקומי (אנגלית)
"CV_PNIM"        // קוד ועד (משרד הפנים)
"CV_LAMAS"       // קוד ועד (למ"ס)
"Machoz"         // מחוז
"Nafa1"          // נפה 1
"Nafa2"          // 2 נפה
"Eshkol_MPn"     // אשכול מוניציפלי
"Sign_Date"      // תאריך אישור/עדכון
"Shape_Leng"     // אורך הגבולות (מטרים)
"Shape_Area"     // שטח (מטרים רבועים)
```
