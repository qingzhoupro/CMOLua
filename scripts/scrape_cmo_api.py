#!/usr/bin/env python3
"""
CMO Lua API 官方文档爬取脚本

功能：从 https://commandlua.github.io/assets/ 爬取所有函数文档，
      输出到 references/lua-api/generated/ 目录下，每个函数一个 .md 文件。

用法：
    python scripts/scrape_cmo_api.py              # 增量爬取（跳过已有文件）
    python scripts/scrape_cmo_api.py --all        # 全量爬取（覆盖已有文件）
    python scripts/scrape_cmo_api.py ScenEdit_AddUnit ScenEdit_GetUnit  # 指定函数

依赖：
    pip install requests beautifulsoup4
"""

import os
import re
import sys
import time
import argparse
from pathlib import Path
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("ERROR: requests 未安装，请运行: pip install requests")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: beautifulsoup4 未安装，请运行: pip install beautifulsoup4")
    sys.exit(1)


BASE_URL = "https://commandlua.github.io/assets/"
INDEX_PAGE = BASE_URL + "Functions.html"

SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR.parent / "references" / "lua-api" / "generated"


# 从 official-api-index.md 提取所有函数名和官方 URL
FUNCTION_LIST = [
    # Unit 操作
    ("ScenEdit_AddUnit", "Function_ScenEdit_AddUnit.html"),
    ("ScenEdit_GetUnit", "Function_ScenEdit_GetUnit.html"),
    ("ScenEdit_SetUnit", "Function_ScenEdit_SetUnit.html"),
    ("ScenEdit_UpdateUnit", "Function_ScenEdit_UpdateUnit.html"),
    ("ScenEdit_DeleteUnit", "Function_ScenEdit_DeleteUnit.html"),
    ("ScenEdit_KillUnit", "Function_ScenEdit_KillUnit.html"),
    ("ScenEdit_SetLoadout", "Function_ScenEdit_SetLoadout.html"),
    ("ScenEdit_GetLoadout", "Function_ScenEdit_GetLoadout.html"),
    ("ScenEdit_SetEMCON", "Function_ScenEdit_SetEMCON.html"),
    ("ScenEdit_SetDoctrine", "Function_ScenEdit_SetDoctrine.html"),
    ("ScenEdit_GetDoctrine", "Function_ScenEdit_GetDoctrine.html"),
    ("ScenEdit_RefuelUnit", "Function_ScenEdit_RefuelUnit.html"),
    ("ScenEdit_AddReloadsToUnit", "Function_ScenEdit_AddReloadsToUnit.html"),
    ("ScenEdit_AddWeaponToUnitMagazine", "Function_ScenEdit_AddWeaponToUnitMagazine.html"),
    ("ScenEdit_FillMagsForLoadout", "Function_ScenEdit_FillMagsForLoadout.html"),
    ("ScenEdit_MergeUnits", "Function_ScenEdit_MergeUnits.html"),
    ("ScenEdit_SplitUnit", "Function_ScenEdit_SplitUnit.html"),
    ("ScenEdit_SetUnitSide", "Function_ScenEdit_SetUnitSide.html"),
    ("ScenEdit_SetUnitDamage", "Function_ScenEdit_SetUnitDamage.html"),
    ("ScenEdit_ClearAllAircraft", "Function_ScenEdit_ClearAllAircraft.html"),
    ("ScenEdit_ClearAllMagazines", "Function_ScenEdit_ClearAllMagazines.html"),
    ("ScenEdit_TransferCargo", "Function_ScenEdit_TransferCargo.html"),
    ("ScenEdit_UnloadCargo", "Function_ScenEdit_UnloadCargo.html"),
    ("ScenEdit_UpdateUnitCargo", "Function_ScenEdit_UpdateUnitCargo.html"),
    ("ScenEdit_HostUnitToParent", "Function_ScenEdit_HostUnitToParent.html"),
    ("ScenEdit_DistributeWeaponAtAirbase", "Function_ScenEdit_DistributeWeaponAtAirbase.html"),
    # Mission 操作
    ("ScenEdit_AddMission", "Function_ScenEdit_AddMission.html"),
    ("ScenEdit_GetMission", "Function_ScenEdit_GetMission.html"),
    ("ScenEdit_SetMission", "Function_ScenEdit_SetMission.html"),
    ("ScenEdit_DeleteMission", "Function_ScenEdit_DeleteMission.html"),
    ("ScenEdit_GetMissions", "Function_ScenEdit_GetMissions.html"),
    ("ScenEdit_AssignUnitToMission", "Function_ScenEdit_AssignUnitToMission.html"),
    ("ScenEdit_RemoveUnitAsTarget", "Function_ScenEdit_RemoveUnitAsTarget.html"),
    ("ScenEdit_AssignUnitAsTarget", "Function_ScenEdit_AssignUnitAsTarget.html"),
    ("ScenEdit_CreateMissionFlightPlan", "Function_ScenEdit_CreateMissionFlightPlan.html"),
    ("ScenEdit_ExportMission", "Function_ScenEdit_ExportMission.html"),
    ("ScenEdit_ImportMission", "Function_ScenEdit_ImportMission.html"),
    # Side 操作
    ("ScenEdit_AddSide", "Function_ScenEdit_AddSide.html"),
    ("ScenEdit_RemoveSide", "Function_ScenEdit_RemoveSide.html"),
    ("ScenEdit_SetSidePosture", "Function_ScenEdit_SetSidePosture.html"),
    ("ScenEdit_GetSidePosture", "Function_ScenEdit_GetSidePosture.html"),
    ("ScenEdit_SetSideOptions", "Function_ScenEdit_SetSideOptions.html"),
    ("ScenEdit_GetSideOptions", "Function_ScenEdit_GetSideOptions.html"),
    ("ScenEdit_GetSideIsHuman", "Function_ScenEdit_GetSideIsHuman.html"),
    ("VP_GetSides", "Function_VP_GetSides.html"),
    ("VP_GetSide", "Function_VP_GetSide.html"),
    ("VP_GetUnit", "Function_VP_GetUnit.html"),
    ("VP_GetContact", "Function_VP_GetContact.html"),
    ("VP_GetScenario", "Function_VP_GetScenario.html"),
    ("ScenEdit_PlayerSide", "Function_ScenEdit_PlayerSide.html"),
    # Event
    ("ScenEdit_SetEvent", "Function_ScenEdit_SetEvent.html"),
    ("ScenEdit_GetEvent", "Function_ScenEdit_GetEvent.html"),
    ("ScenEdit_GetEvents", "Function_ScenEdit_GetEvents.html"),
    ("ScenEdit_SetTrigger", "Function_ScenEdit_SetTrigger.html"),
    ("ScenEdit_SetCondition", "Function_ScenEdit_SetCondition.html"),
    ("ScenEdit_SetAction", "Function_ScenEdit_SetAction.html"),
    ("ScenEdit_SetEventTrigger", "Function_ScenEdit_SetEventTrigger.html"),
    ("ScenEdit_SetEventCondition", "Function_ScenEdit_SetEventCondition.html"),
    ("ScenEdit_SetEventAction", "Function_ScenEdit_SetEventAction.html"),
    ("ScenEdit_AddSpecialAction", "Function_ScenEdit_AddSpecialAction.html"),
    ("ScenEdit_GetSpecialAction", "Function_ScenEdit_GetSpecialAction.html"),
    ("ScenEdit_ExecuteSpecialAction", "Function_ScenEdit_ExecuteSpecialAction.html"),
    ("ScenEdit_ExecuteEventAction", "Function_ScenEdit_ExecuteEventAction.html"),
    ("ScenEdit_UnitX", "Function_ScenEdit_UnitX.html"),
    ("ScenEdit_UnitC", "Function_ScenEdit_UnitC.html"),
    ("ScenEdit_UnitY", "Function_ScenEdit_UnitY.html"),
    ("ScenEdit_EventX", "Function_ScenEdit_EventX.html"),
    # Contact
    ("ScenEdit_GetContact", "Function_ScenEdit_GetContact.html"),
    ("ScenEdit_GetContacts", "Function_ScenEdit_GetContacts.html"),
    ("ScenEdit_AttackContact", "Function_ScenEdit_AttackContact.html"),
    # Reference Point
    ("ScenEdit_AddReferencePoint", "Function_ScenEdit_AddReferencePoint.html"),
    ("ScenEdit_GetReferencePoint", "Function_ScenEdit_GetReferencePoint.html"),
    ("ScenEdit_GetReferencePoints", "Function_ScenEdit_GetReferencePoints.html"),
    ("ScenEdit_SetReferencePoint", "Function_ScenEdit_SetReferencePoint.html"),
    ("ScenEdit_DeleteReferencePoint", "Function_ScenEdit_DeleteReferencePoint.html"),
    # Zone
    ("ScenEdit_AddZone", "Function_ScenEdit_AddZone.html"),
    ("ScenEdit_SetZone", "Function_ScenEdit_SetZone.html"),
    ("ScenEdit_RemoveZone", "Function_ScenEdit_RemoveZone.html"),
    ("ScenEdit_TransformZone", "Function_ScenEdit_TransformZone.html"),
    # Tool
    ("Tool_Range", "Function_Tool_Range.html"),
    ("Tool_Bearing", "Function_Tool_Bearing.html"),
    ("Tool_LOS", "Function_Tool_LOS.html"),
    ("Tool_LOS_Points", "Function_Tool_LOS_Points.html"),
    ("World_GetPointFromBearing", "Function_World_GetPointFromBearing.html"),
    ("World_GetElevation", "Function_World_GetElevation.html"),
    ("World_GetLocation", "Function_World_GetLocation.html"),
    ("World_GetCircleFromPoint", "Function_World_GetCircleFromPoint.html"),
    # Scenario
    ("GetScenarioTitle", "Function_GetScenarioTitle.html"),
    ("ScenEdit_CurrentTime", "Function_ScenEdit_CurrentTime.html"),
    ("ScenEdit_CurrentLocalTime", "Function_ScenEdit_CurrentLocalTime.html"),
    ("ScenEdit_EndScenario", "Function_ScenEdit_EndScenario.html"),
    ("ScenEdit_GetScenHasStarted", "Function_ScenEdit_GetScenHasStarted.html"),
    ("ScenEdit_GetWeather", "Function_ScenEdit_GetWeather.html"),
    ("ScenEdit_SetWeather", "Function_ScenEdit_SetWeather.html"),
    ("ScenEdit_GetScore", "Function_ScenEdit_GetScore.html"),
    ("ScenEdit_SetScore", "Function_ScenEdit_SetScore.html"),
    ("ScenEdit_GetTimeOfDay", "Function_ScenEdit_GetTimeOfDay.html"),
    ("ScenEdit_SetStartTime", "Function_ScenEdit_SetStartTime.html"),
    ("ScenEdit_SetTime", "Function_ScenEdit_SetTime.html"),
    ("ScenEdit_GetDateTimeTicks", "Function_ScenEdit_GetDateTimeTicks.html"),
    # UI
    ("ScenEdit_MsgBox", "Function_ScenEdit_MsgBox.html"),
    ("ScenEdit_InputBox", "Function_ScenEdit_InputBox.html"),
    ("ScenEdit_SpecialMessage", "Function_ScenEdit_SpecialMessage.html"),
    ("ScenEdit_CreateBarkNotification_Geo", "Function_ScenEdit_CreateBarkNotification_Geo.html"),
    ("ScenEdit_CreateBarkNotification_Geo_Bulk", "Function_ScenEdit_CreateBarkNotification_Geo_Bulk.html"),
    ("ScenEdit_CreateBarkNotification_Unit", "Function_ScenEdit_CreateBarkNotification_Unit.html"),
    ("ScenEdit_CreateBarkNotification_Unit_Bulk", "Function_ScenEdit_CreateBarkNotification_Unit_Bulk.html"),
    ("UI_SetCameraView", "Function_UI_SetCameraView.html"),
    ("UI_SelectThisUnit", "Function_UI_SelectThisUnit.html"),
    ("UI_SelectUnitsPrompt_FromSides", "Function_UI_SelectUnitsPrompt_FromSides.html"),
    ("UI_SelectUnitsPrompt_OwnSide", "Function_UI_SelectUnitsPrompt_OwnSide.html"),
    ("UI_OpenNewDatabaseWindow", "Function_UI_OpenNewDatabaseWindow.html"),
    ("Tool_ResetMessageLog", "Function_Tool_ResetMessageLog.html"),
    ("Tool_UIwindow", "Function_Tool_UIwindow.html"),
    # Storage
    ("ScenEdit_SetKeyValue", "Function_ScenEdit_SetKeyValue.html"),
    ("ScenEdit_GetKeyValue", "Function_ScenEdit_GetKeyValue.html"),
    ("ScenEdit_ClearKeyValue", "Function_ScenEdit_ClearKeyValue.html"),
    # Minefield
    ("ScenEdit_AddMinefield", "Function_ScenEdit_AddMinefield.html"),
    ("ScenEdit_DeleteMinefield", "Function_ScenEdit_DeleteMinefield.html"),
    ("ScenEdit_GetMinefield", "Function_ScenEdit_GetMinefield.html"),
    ("ScenEdit_DeleteMine", "Function_ScenEdit_DeleteMine.html"),
    # Other
    ("Command_SaveScen", "Function_Command_SaveScen.html"),
    ("GetBuildNumber", "Function_GetBuildNumber.html"),
    ("ScenEdit_RunScript", "Function_ScenEdit_RunScript.html"),
    ("ScenEdit_ExportInst", "Function_ScenEdit_ExportInst.html"),
    ("ScenEdit_ImportInst", "Function_ScenEdit_ImportInst.html"),
    ("ScenEdit_UpdateRSetting", "Function_ScenEdit_UpdateRSetting.html"),
    ("ScenEdit_UseAttachment", "Function_ScenEdit_UseAttachment.html"),
    ("ScenEdit_UseAttachmentOnSide", "Function_ScenEdit_UseAttachmentOnSide.html"),
    ("ScenEdit_AddExplosion", "Function_ScenEdit_AddExplosion.html"),
    ("ScenEdit_AddCustomLoss", "Function_ScenEdit_AddCustomLoss.html"),
    ("SetScenarioTitle", "Function_SetScenarioTitle.html"),
    ("VP_SetTimeCompression", "Function_VP_SetTimeCompression.html"),
    ("Tool_BuildBlankScenario", "Function_Tool_BuildBlankScenario.html"),
    ("Tool_DumpEvents", "Function_Tool_DumpEvents.html"),
    ("Tool_EmulateNoConsole", "Function_Tool_EmulateNoConsole.html"),
    ("Tool_QueryRCS", "Function_Tool_QueryRCS.html"),
    ("Tool_QuerySoundLevel", "Function_Tool_QuerySoundLevel.html"),
    ("Exporter_SetSetting", "Function_Exporter_SetSetting.html"),
    # EMCON
    ("ScenEdit_ClearAllSideUnitsEmconConfigs", "Function_ScenEdit_ClearAllSideUnitsEmconConfigs.html"),
    ("ScenEdit_ClearUnitEmconConfigs", "Function_ScenEdit_ClearUnitEmconConfigs.html"),
    ("ScenEdit_DuplicateEmconConfigToSide", "Function_ScenEdit_DuplicateEmconConfigToSide.html"),
    ("ScenEdit_DuplicateEmconConfigToUnit", "Function_ScenEdit_DuplicateEmconConfigToUnit.html"),
    ("ScenEdit_GetUnitIntermittentEmissionConfig", "Function_ScenEdit_GetUnitIntermittentEmissionConfig.html"),
    ("ScenEdit_SetSideEmconAlertness", "Function_ScenEdit_SetSideEmconAlertness.html"),
    ("ScenEdit_SetUnitIntermittentEmissionConfig", "Function_ScenEdit_SetUnitIntermittentEmissionConfig.html"),
    ("ScenEdit_SwitchUnitIntermittentEmission", "Function_ScenEdit_SwitchUnitIntermittentEmission.html"),
    # Doctrine WRA
    ("ScenEdit_GetDoctrineWRA", "Function_ScenEdit_GetDoctrineWRA.html"),
    ("ScenEdit_SetDoctrineWRA", "Function_ScenEdit_SetDoctrineWRA.html"),
    # Formation
    ("ScenEdit_GetFormation", "Function_ScenEdit_GetFormation.html"),
    # Weapon Allocation
    ("ScenEdit_WeaponAllocation", "Function_ScenEdit_WeaponAllocation.html"),
    # Misc
    ("ScenEdit_SelectedUnits", "Function_ScenEdit_SelectedUnits.html"),
    ("ScenEdit_AddSpecialAction", "Function_ScenEdit_AddSpecialAction.html"),
    ("ScenEdit_GetSpecialAction", "Function_ScenEdit_GetSpecialAction.html"),
    ("ScenEdit_ExecuteSpecialAction", "Function_ScenEdit_ExecuteSpecialAction.html"),
    ("UI_CallAdvancedDialog", "Function_UI_CallAdvancedDialog.html"),
    ("UI_CallAdvancedHTMLDialog", "Function_UI_CallAdvancedHTMLDialog.html"),
]


def fetch_page(url: str, timeout: int = 15) -> str | None:
    """获取页面内容，失败返回 None"""
    try:
        resp = requests.get(url, timeout=timeout, headers={
            "User-Agent": "Mozilla/5.0 (compatible; CMO-Lua-Doc-Scraper/1.0)"
        })
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  [WARN] 获取失败 {url}: {e}")
        return None


def parse_function_page(func_name: str, html: str, url: str) -> str:
    """解析函数页面，生成 Markdown 文档"""
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h2") or soup.find("h1") or soup.find("h3")
    if not title:
        title_text = f"Function {func_name}"
    else:
        title_text = title.get_text(strip=True)

    # 提取正文内容（跳过导航和脚注）
    main_content = []
    found_content = False

    for elem in soup.find_all(["h2", "h3", "h4", "p", "pre", "code", "ul", "ol", "table"]):
        text = elem.get_text("\n", strip=True)
        if not text:
            continue

        # 跳过版权和导航
        if any(kw in text for kw in ["Copyright", "Command Lua Docs", "Reference Forum", "News",
                                       "Introduction", "How to Use", "First Steps", "External Resources",
                                       "Overview", "Case Sensitivity", "Event Handling", "Error Handling",
                                       "Data Types", "Functions", "Wrappers", "Tables"]):
            if not found_content:
                continue
            else:
                break

        # 标记代码块
        if elem.name == "pre":
            code_text = elem.get_text("\n", strip=True)
            # 清理 HTML entity
            code_text = code_text.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
            code_text = code_text.replace("&quot;", '"').replace("&#39;", "'")
            main_content.append("```lua")
            main_content.append(code_text)
            main_content.append("```")
            found_content = True
        elif elem.name == "code":
            code_text = elem.get_text("\n", strip=True)
            code_text = code_text.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
            main_content.append(f"`{code_text}`")
        elif elem.name in ("h2", "h3", "h4"):
            main_content.append(f"\n### {text}\n")
            found_content = True
        elif elem.name in ("p",):
            main_content.append(f"\n{text}\n")
            found_content = True
        elif elem.name in ("ul", "ol"):
            for li in elem.find_all("li", recursive=False):
                li_text = li.get_text("\n", strip=True)
                li_text = li_text.replace("&gt;", ">").replace("&lt;", "<")
                main_content.append(f"- {li_text}")
            found_content = True
        elif elem.name == "table":
            rows = elem.find_all("tr")
            if rows:
                # 提取表头
                headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
                main_content.append("")
                main_content.append("| " + " | ".join(headers) + " |")
                main_content.append("| " + " | ".join(["---"] * len(headers)) + " |")
                for row in rows[1:]:
                    cells = [td.get_text(strip=True) for td in row.find_all(["th", "td"])]
                    main_content.append("| " + " | ".join(cells) + " |")
                main_content.append("")
                found_content = True

    # 如果没有提取到内容，尝试直接提取 body
    if not found_content:
        body = soup.find("body")
        if body:
            raw_text = body.get_text("\n", strip=True)
            # 清理
            raw_text = raw_text.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
            raw_text = raw_text.replace("&quot;", '"').replace("&#39;", "'")
            main_content.append(raw_text)

    content_body = "\n".join(main_content)

    # 构建输出 Markdown
    output = f"""# {func_name}

> 官方文档来源: [{url}]({url})  
> 爬取时间: {time.strftime('%Y-%m-%d %H:%M:%S')}  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---

{content_body}

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
"""

    return output


def scrape_function(func_name: str, filename: str, force: bool = False) -> bool:
    """爬取单个函数文档"""
    url = BASE_URL + filename
    out_path = OUTPUT_DIR / f"{func_name}.md"

    # 增量模式：跳过已有文件
    if not force and out_path.exists():
        return False

    print(f"  爬取 {func_name} <- {url}")

    html = fetch_page(url)
    if html is None:
        print(f"  [SKIP] {func_name} 获取失败，跳过")
        return False

    content = parse_function_page(func_name, html, url)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="爬取 CMO Lua 官方文档到 generated/ 目录"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="全量爬取（覆盖已有文件，默认增量）"
    )
    parser.add_argument(
        "--delay", type=float, default=1.0,
        help="请求间隔秒数（默认 1.0）"
    )
    parser.add_argument(
        "functions", nargs="*",
        help="指定要爬取的函数名（如 ScenEdit_AddUnit）"
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 确定要爬取的函数列表
    if args.functions:
        func_map = {name: fname for name, fname in FUNCTION_LIST}
        targets = []
        for f in args.functions:
            if f in func_map:
                targets.append((f, func_map[f]))
            else:
                print(f"[WARN] 未知函数: {f}，跳过")
    else:
        targets = FUNCTION_LIST

    print(f"共 {len(targets)} 个函数待爬取")
    print(f"输出目录: {OUTPUT_DIR}")
    print(f"模式: {'全量' if args.all else '增量（跳过已有）'}")
    print()

    success = 0
    skipped = 0
    failed = 0

    for func_name, filename in targets:
        result = scrape_function(func_name, filename, force=args.all)
        if result:
            success += 1
        elif not args.all and (OUTPUT_DIR / f"{func_name}.md").exists():
            skipped += 1
        else:
            failed += 1

        if result:
            time.sleep(args.delay)

    print()
    print("=" * 50)
    print(f"完成: 成功 {success}, 跳过 {skipped}, 失败 {failed}")
    print(f"输出目录: {OUTPUT_DIR}")

    # 列出已生成的文件
    md_files = sorted(OUTPUT_DIR.glob("*.md"))
    print(f"当前共有 {len(md_files)} 个文档")


if __name__ == "__main__":
    main()
