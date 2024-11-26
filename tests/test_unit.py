from infrastructure.stack import app_service_plan

def test_app_service_plan_tier():
    def check_tier(tier):
        assert tier == "Free", "App Service Plan sollte im Free-Tier sein"
    app_service_plan.sku.tier.apply(check_tier)
