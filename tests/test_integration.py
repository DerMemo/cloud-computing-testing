from infrastructure.stack import web_app, app_service_plan

def test_web_app_uses_correct_plan():
    def check_plan(server_farm_id, plan_id):
        assert server_farm_id == plan_id, "Web App sollte mit dem korrekten App Service Plan verknüpft sein"
    web_app.server_farm_id.apply(lambda server_farm_id:
        app_service_plan.id.apply(lambda plan_id: check_plan(server_farm_id, plan_id))
    )
