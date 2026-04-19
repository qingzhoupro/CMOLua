--[[
  File: examples/contributed/airbase-generator/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Airbase creation logic inspired by CMO Community Scripts
  - DBID references sourced from Matrix Games database documentation

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 机场设施自动生成

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心函数

```lua
F_CreateAirBase(sideName, basename, latlonTable, runways, taxiways, accesspoints, tarmacspaces, ammopads)
```

### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| `sideName` | string | 阵营名称 |
| `basename` | string | 基地总名称（用于归组） |
| `latlonTable` | table | 经纬度表 `{latitude=x, longitude=y}` |
| `runways` | number | 跑道数量 |
| `taxiways` | number | 滑行道数量 |
| `accesspoints` | number | 进入点数量 |
| `tarmacspaces` | number | 停机坪数量 |
| `ammopads` | number | 弹药库数量 |

---

## 完整代码

```lua
-- ============================================================
-- 机场设施自动生成函数
-- AI 助手提示：各 DBID 需通过 MCP query_dbid 查询
-- ============================================================

function F_CreateAirBase(sideName, basename, latlonTable, runways, taxiways, accesspoints, tarmacspaces, ammopads)
    local side_name = sideName
    local lat = latlonTable['latitude']
    local lon = latlonTable['longitude']

    -- 1. 跑道
    -- ⚠️ ⚠️ ⚠️ DBID 需通过 query_dbid("跑道") 查询
    local RUNWAY_DBID = {{RUNWAY_DBID}}
    for i = 1, runways do
        local u = ScenEdit_AddUnit({
            side = side_name,
            type = 'Facility',
            name = 'Runway ' .. i,
            dbid = RUNWAY_DBID,
            autodetectable = true,
            Lat = lat,
            Lon = lon
        })
        u.group = basename
        lat = lat + .004
    end
    print('Runway ok')

    -- 重置经纬度，偏移创建滑行道
    lat = latlonTable['latitude']
    lon = latlonTable['longitude'] + .002

    -- 2. 滑行道
    -- ⚠️ ⚠️ ⚠️ DBID 需通过 query_dbid("滑行道") 查询
    local TAXIWAY_DBID = {{TAXIWAY_DBID}}
    for i = 1, taxiways do
        local u = ScenEdit_AddUnit({
            side = side_name,
            type = 'Facility',
            name = 'Taxiway ' .. i,
            dbid = TAXIWAY_DBID,
            autodetectable = true,
            Lat = lat,
            Lon = lon
        })
        u.group = basename
        lat = lat + .004
    end
    print('Taxiway ok')

    -- 重置经纬度，偏移创建进入点
    lat = latlonTable['latitude']
    lon = latlonTable['longitude'] + .004

    -- 3. 进入点
    -- ⚠️ ⚠️ ⚠️ DBID 需通过 query_dbid("进入点") 或 query_dbid("parking") 查询
    local ACCESSPOINT_DBID = {{ACCESSPOINT_DBID}}
    for i = 1, accesspoints do
        local u = ScenEdit_AddUnit({
            side = side_name,
            type = 'Facility',
            name = 'Access Point ' .. i,
            dbid = ACCESSPOINT_DBID,
            autodetectable = true,
            Lat = lat,
            Lon = lon
        })
        u.group = basename
        lat = lat + .004
    end
    print('Access Point ok')

    -- 重置经纬度，偏移创建停机坪
    lat = latlonTable['latitude']
    lon = latlonTable['longitude'] + .006

    -- 4. 停机坪
    -- ⚠️ ⚠️ ⚠️ DBID 需通过 query_dbid("停机坪") 查询
    local TARMAC_DBID = {{TARMAC_DBID}}
    for i = 1, tarmacspaces do
        local u = ScenEdit_AddUnit({
            side = side_name,
            type = 'Facility',
            name = 'Tarmac Space ' .. i,
            dbid = TARMAC_DBID,
            autodetectable = true,
            Lat = lat,
            Lon = lon
        })
        u.group = basename
        lat = lat + .002
    end
    print('Tarmac Space ok')

    -- 重置经纬度，偏移创建弹药库
    lat = latlonTable['latitude']
    lon = latlonTable['longitude'] + .008

    -- 5. 弹药库
    -- ⚠️ ⚠️ ⚠️ DBID 需通过 query_dbid("弹药库") 或 query_dbid("ammo") 查询
    local AMMO_DBID = {{AMMO_DBID}}
    for i = 1, ammopads do
        local u = ScenEdit_AddUnit({
            side = side_name,
            type = 'Facility',
            name = 'Ammo Pad ' .. i,
            dbid = AMMO_DBID,
            autodetectable = true,
            Lat = lat,
            Lon = lon
        })
        u.group = basename
        lat = lat + .002
    end
    print('Ammo Pad ok')

    print('机场创建完成: ' .. basename)
end
```

---

## 调用示例

```lua
-- ============================================================
-- 创建机场
-- AI 助手提示：调用前需确保各 DBID 已替换为实际查询值
-- ============================================================

-- 示例：创建{{BASE_NAME}}机场
-- 参数：阵营、基地名、经纬度、跑道数、滑行道数、进入点数、停机坪数、弹药库数
F_CreateAirBase(
    "{{SIDE}}",                                    -- 阵营
    "{{BASE_NAME}}",                               -- 基地总名称
    {latitude = {{BASE_LAT}}, longitude = {{BASE_LON}}},  -- 经纬度
    {{RUNWAY_COUNT}},                               -- 跑道数
    {{TAXIWAY_COUNT}},                             -- 滑行道数
    {{ACCESSPOINT_COUNT}},                         -- 进入点数
    {{TARMAC_COUNT}},                              -- 停机坪数
    {{AMMO_COUNT}}                                 -- 弹药库数
)
```

---

## ⚠️ 常见错误

**错误信息**：`The requested object has been deprecated in the database`

**原因**：DBID 已过时，对应装备在当前 CMO 数据库版本中已变更。

**解决**：使用 MCP `query_dbid()` 查询正确的 DBID。

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE}}` | 阵营名称 | `"Blue"` |
| `{{BASE_NAME}}` | 基地总名称 | `"Osan AB"` |
| `{{BASE_LAT}}` | 基地纬度（数字） | `37.5` |
| `{{BASE_LON}}` | 基地经度（数字） | `127.0` |
| `{{RUNWAY_DBID}}` | 跑道 DBID（数字） | `945` |
| `{{TAXIWAY_DBID}}` | 滑行道 DBID（数字） | `1425` |
| `{{ACCESSPOINT_DBID}}` | 进入点 DBID（数字） | `307` |
| `{{TARMAC_DBID}}` | 停机坪 DBID（数字） | `281` |
| `{{AMMO_DBID}}` | 弹药库 DBID（数字） | `1496` |
| `{{RUNWAY_COUNT}}` | 跑道数量（数字） | `2` |
| `{{TAXIWAY_COUNT}}` | 滑行道数量（数字） | `2` |
| `{{ACCESSPOINT_COUNT}}` | 进入点数量（数字） | `4` |
| `{{TARMAC_COUNT}}` | 停机坪数量（数字） | `8` |
| `{{AMMO_COUNT}}` | 弹药库数量（数字） | `2` |
