import pytest


# Basic
@pytest.mark.parametrize("route", ["/", "/daniel-mizsak", "/mentors", "/faq"])
def test_basic_routes(client, route):
    respond = client.get(route)
    assert respond.status_code == 200


# Categories, subcategories, lessons and assessments
post_routes = [f"/pv/{category}/" for category in ("python", "extra", "project")]
python_routes = {
    "python_alapjai": [
        "00_Bevezetes_es_kurzusinformaciok",
        "01_A_Python_programozasi_nyelvrol",
        "02_Valtozok_tipusok_es_muveleteik",
        "03_Komment_kiiras_bekeres",
        "04_Lista_es_dictionary",
    ],
}
for subcategory in python_routes:
    post_routes.append(f"/pv/python/{subcategory}/")
    for lesson in python_routes[subcategory]:
        post_routes.append(f"/pv/python/{subcategory}/{lesson}/")  # noqa: PERF401


@pytest.mark.parametrize("route", post_routes)
def test_posts(client, route):
    respond = client.get(route)
    assert respond.status_code == 200


# Error handlers
@pytest.mark.parametrize(
    ("route", "error"),
    [("/non-existing-route", 404)],
)
def test_error_handler(client, route, error):
    respond = client.get(route)
    assert respond.status_code == error


# Database
# TODO: Test other properties like projects, database and forms
