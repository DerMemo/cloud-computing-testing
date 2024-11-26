import pulumi
from pulumi_azure_native import resources, web

# Ressourcen definieren
resource_group = resources.ResourceGroup("myResourceGroup")
app_service_plan = web.AppServicePlan(
    "myAppServicePlan",
    resource_group_name=resource_group.name,
    kind="Linux",
    reserved=True,
    sku=web.SkuDescriptionArgs(
        name="F1",
        tier="Free",
        capacity=1,
    ),
)
web_app = web.WebApp(
    "myWebApp",
    resource_group_name=resource_group.name,
    server_farm_id=app_service_plan.id,
    site_config=web.SiteConfigArgs(
        linux_fx_version="PYTHON|3.8",
    ),
)

# Pulumi-Outputs nur exportieren, wenn im Pulumi-Kontext
if __name__ == "__main__":
    pulumi.export("resource_group_name", resource_group.name)
    pulumi.export("app_service_plan_name", app_service_plan.name)
    pulumi.export("web_app_url", web_app.default_host_name.apply(lambda name: f"http://{name}"))
