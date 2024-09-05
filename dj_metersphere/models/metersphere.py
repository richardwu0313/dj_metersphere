# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiCaseExecutionInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    source_id = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    trigger_mode = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField()
    project_id = models.CharField(max_length=50, blank=True, null=True)
    execute_type = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_case_execution_info'


class ApiDataView(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    report_id = models.CharField(max_length=255)
    api_name = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    response_code = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    response_time = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_data_view'


class ApiDefinition(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=64)
    protocol = models.CharField(max_length=255)
    path = models.CharField(max_length=1000, blank=True, null=True)
    module_path = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    environment_id = models.CharField(max_length=50, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    module_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    num = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    original_state = models.CharField(max_length=64, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    case_total = models.CharField(max_length=100, blank=True, null=True)
    case_status = models.CharField(max_length=100, blank=True, null=True)
    case_passing_rate = models.CharField(max_length=100, blank=True, null=True)
    delete_time = models.BigIntegerField(blank=True, null=True)
    delete_user_id = models.CharField(max_length=64, blank=True, null=True)
    order = models.BigIntegerField()
    remark = models.TextField(blank=True, null=True)
    version_id = models.CharField(max_length=50, blank=True, null=True)
    ref_id = models.CharField(max_length=50, blank=True, null=True)
    latest = models.IntegerField(blank=True, null=True)
    to_be_updated = models.IntegerField(blank=True, null=True)
    to_be_update_time = models.BigIntegerField(db_column='to_be_update_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_definition'


class ApiDefinitionEnv(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=50)
    env_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_definition_env'


class ApiDefinitionExecResult(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255, blank=True, null=True)
    resource_id = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField()
    create_time = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    actuator = models.CharField(max_length=100, blank=True, null=True)
    trigger_mode = models.CharField(max_length=50, blank=True, null=True)
    error_code = models.CharField(max_length=255, blank=True, null=True)
    version_id = models.CharField(max_length=50, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    integrated_report_id = models.CharField(max_length=50, blank=True, null=True)
    report_type = models.CharField(max_length=100)
    env_config = models.TextField(blank=True, null=True)
    relevance_test_plan_report_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_definition_exec_result'


class ApiDefinitionFollow(models.Model):
    definition_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_definition_follow'
        unique_together = (('definition_id', 'follow_id'),)


class ApiExecutionInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    source_id = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    create_time = models.BigIntegerField()
    project_id = models.CharField(max_length=50, blank=True, null=True)
    execute_type = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_execution_info'


class ApiExecutionQueue(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    report_id = models.CharField(max_length=100, blank=True, null=True)
    report_type = models.CharField(max_length=100, blank=True, null=True)
    run_mode = models.CharField(max_length=100, blank=True, null=True)
    pool_id = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    failure = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_execution_queue'


class ApiExecutionQueueDetail(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    queue_id = models.CharField(max_length=100, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    report_id = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.CharField(max_length=100, blank=True, null=True)
    evn_map = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    retry_enable = models.IntegerField(blank=True, null=True)
    retry_number = models.BigIntegerField(blank=True, null=True)
    project_ids = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_execution_queue_detail'


class ApiLoadTest(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    api_id = models.CharField(max_length=255)
    load_test_id = models.CharField(max_length=50)
    env_id = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20)
    api_version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_load_test'


class ApiModule(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    protocol = models.CharField(max_length=64)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    pos = models.FloatField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_module'


class ApiScenario(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    project_id = models.CharField(max_length=50)
    tags = models.CharField(max_length=2000, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    api_scenario_module_id = models.CharField(max_length=64, blank=True, null=True)
    module_path = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    step_total = models.IntegerField(blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    scenario_definition = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pass_rate = models.CharField(max_length=100, blank=True, null=True)
    last_result = models.CharField(max_length=100, blank=True, null=True)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    original_state = models.CharField(max_length=64, blank=True, null=True)
    custom_num = models.CharField(max_length=64, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    delete_time = models.BigIntegerField(blank=True, null=True)
    delete_user_id = models.CharField(max_length=64, blank=True, null=True)
    execute_times = models.IntegerField(blank=True, null=True)
    order = models.BigIntegerField()
    environment_type = models.CharField(max_length=20, blank=True, null=True)
    environment_json = models.TextField(blank=True, null=True)
    environment_group_id = models.CharField(max_length=50, blank=True, null=True)
    version_id = models.CharField(max_length=50, blank=True, null=True)
    ref_id = models.CharField(max_length=255, blank=True, null=True)
    latest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario'


class ApiScenarioFollow(models.Model):
    scenario_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario_follow'
        unique_together = (('scenario_id', 'follow_id'),)


class ApiScenarioModule(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    pos = models.FloatField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario_module'


class ApiScenarioReferenceId(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    api_scenario_id = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    create_user_id = models.CharField(max_length=64, blank=True, null=True)
    reference_id = models.CharField(max_length=255, blank=True, null=True)
    reference_type = models.CharField(max_length=255, blank=True, null=True)
    data_type = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    method = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario_reference_id'


class ApiScenarioReport(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=3000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    status = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    trigger_mode = models.CharField(max_length=64, blank=True, null=True)
    execute_type = models.CharField(max_length=200, blank=True, null=True)
    scenario_name = models.CharField(max_length=3000, blank=True, null=True)
    scenario_id = models.CharField(max_length=3000, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    actuator = models.CharField(max_length=100, blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    report_version = models.IntegerField(blank=True, null=True)
    version_id = models.CharField(max_length=50, blank=True, null=True)
    report_type = models.CharField(max_length=100, blank=True, null=True)
    env_config = models.TextField(blank=True, null=True)
    relevance_test_plan_report_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario_report'


class ApiScenarioReportDetail(models.Model):
    report_id = models.CharField(primary_key=True, max_length=64)
    project_id = models.CharField(max_length=64)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario_report_detail'


class ApiScenarioReportResult(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    resource_id = models.CharField(max_length=200, blank=True, null=True)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    request_time = models.BigIntegerField(blank=True, null=True)
    total_assertions = models.BigIntegerField(blank=True, null=True)
    pass_assertions = models.BigIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    error_code = models.CharField(max_length=255, blank=True, null=True)
    base_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario_report_result'


class ApiScenarioReportStructure(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    resource_tree = models.TextField(blank=True, null=True)
    console = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_scenario_report_structure'


class ApiSyncRuleRelation(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    resource_id = models.CharField(max_length=50)
    resource_type = models.CharField(max_length=50)
    show_update_rule = models.IntegerField(blank=True, null=True)
    api_sync_case_request = models.TextField(blank=True, null=True)
    case_creator = models.IntegerField(blank=True, null=True)
    scenario_creator = models.IntegerField(blank=True, null=True)
    sync_case = models.IntegerField(blank=True, null=True)
    send_notice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_sync_rule_relation'


class ApiTemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)
    system = models.IntegerField(blank=True, null=True)
    global_field = models.IntegerField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_template'


class ApiTest(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)
    scenario_definition = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'api_test'


class ApiTestCase(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=64)
    api_definition_id = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    create_user_id = models.CharField(max_length=64, blank=True, null=True)
    update_user_id = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    num = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    last_result_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    original_status = models.CharField(max_length=50, blank=True, null=True)
    delete_time = models.BigIntegerField(blank=True, null=True)
    delete_user_id = models.CharField(max_length=64, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    order = models.BigIntegerField()
    case_status = models.CharField(max_length=100, blank=True, null=True)
    version_id = models.CharField(max_length=50, blank=True, null=True)
    to_be_updated = models.IntegerField(blank=True, null=True)
    to_be_update_time = models.BigIntegerField(db_column='to_be_update_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_test_case'


class ApiTestCaseFollow(models.Model):
    case_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_case_follow'
        unique_together = (('case_id', 'follow_id'),)


class ApiTestEnvironment(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=64)
    project_id = models.CharField(max_length=50)
    protocol = models.CharField(max_length=20, blank=True, null=True)
    socket = models.CharField(max_length=225, blank=True, null=True)
    domain = models.CharField(max_length=225, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    variables = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    config = models.TextField(blank=True, null=True)
    hosts = models.TextField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_environment'


class ApiTestFile(models.Model):
    test_id = models.CharField(max_length=64, blank=True, null=True)
    file_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_file'
        unique_together = (('test_id', 'file_id'),)


class ApiTestReport(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    status = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    trigger_mode = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_report'


class ApiTestReportDetail(models.Model):
    report_id = models.CharField(primary_key=True, max_length=64)
    test_id = models.CharField(max_length=64)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_test_report_detail'


class ApiVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_version'


class AttachmentModuleRelation(models.Model):
    relation_id = models.CharField(max_length=64)
    relation_type = models.CharField(max_length=64)
    attachment_id = models.CharField(max_length=50, blank=True, null=True)
    file_metadata_ref_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment_module_relation'


class AuthSource(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    configuration = models.TextField()
    status = models.CharField(max_length=64)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_source'


class CustomField(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=64)
    scene = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    remark = models.CharField(max_length=255, blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    system = models.IntegerField(blank=True, null=True)
    global_field = models.IntegerField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(max_length=64, blank=True, null=True)
    third_part = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field'


class CustomFieldApi(models.Model):
    resource_id = models.CharField(primary_key=True, max_length=50)
    field_id = models.CharField(max_length=50)
    value = models.CharField(max_length=500, blank=True, null=True)
    text_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_field_api'
        unique_together = (('resource_id', 'field_id'),)


class CustomFieldIssues(models.Model):
    resource_id = models.CharField(primary_key=True, max_length=50)
    field_id = models.CharField(max_length=50)
    value = models.CharField(max_length=500, blank=True, null=True)
    text_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_field_issues'
        unique_together = (('resource_id', 'field_id'),)


class CustomFieldTemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    field_id = models.CharField(max_length=50)
    template_id = models.CharField(max_length=50)
    scene = models.CharField(max_length=30)
    required = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    custom_data = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_field_template'


class CustomFieldTestCase(models.Model):
    resource_id = models.CharField(primary_key=True, max_length=50)
    field_id = models.CharField(max_length=50)
    value = models.CharField(max_length=500, blank=True, null=True)
    text_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_field_test_case'
        unique_together = (('resource_id', 'field_id'),)


class CustomFunction(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_function'


class EnterpriseTestReport(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=64, blank=True, null=True)
    update_user = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=64, blank=True, null=True)
    send_freq = models.CharField(max_length=64, blank=True, null=True)
    send_cron = models.CharField(max_length=64, blank=True, null=True)
    last_send_time = models.BigIntegerField(blank=True, null=True)
    report_content = models.TextField(blank=True, null=True)
    addressee = models.TextField(blank=True, null=True)
    duplicated = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_test_report'


class EnterpriseTestReportSendRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    enterprise_test_report_id = models.CharField(max_length=50)
    create_time = models.BigIntegerField()
    create_user = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    report_content = models.TextField(blank=True, null=True)
    addressee = models.TextField(blank=True, null=True)
    duplicated = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_test_report_send_record'


class EnvironmentGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    workspace_id = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'environment_group'


class EnvironmentGroupProject(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    environment_group_id = models.CharField(max_length=50, blank=True, null=True)
    environment_id = models.CharField(max_length=50, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'environment_group_project'


class ErrorReportLibrary(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=64, blank=True, null=True)
    update_user = models.CharField(max_length=64, blank=True, null=True)
    error_code = models.CharField(max_length=255)
    match_type = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_report_library'


class EsbApiParams(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    resource_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    data_struct = models.TextField(blank=True, null=True)
    fronted_script = models.TextField(blank=True, null=True)
    response_data_struct = models.TextField(blank=True, null=True)
    backed_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'esb_api_params'


class FileAssociation(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(max_length=50)
    source_id = models.CharField(max_length=50)
    source_item_id = models.CharField(max_length=50)
    file_metadata_id = models.CharField(max_length=50)
    file_type = models.CharField(max_length=50)
    project_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'file_association'


class FileAttachmentMetadata(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=64, blank=True, null=True)
    size = models.BigIntegerField()
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    creator = models.CharField(max_length=50)
    file_path = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'file_attachment_metadata'


class FileContent(models.Model):
    file_id = models.CharField(primary_key=True, max_length=64)
    file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_content'


class FileMetadata(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=64, blank=True, null=True)
    size = models.BigIntegerField()
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    project_id = models.CharField(max_length=50, blank=True, null=True)
    storage = models.CharField(max_length=50, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=2000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    module_id = models.CharField(max_length=50, blank=True, null=True)
    load_jar = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=1000, blank=True, null=True)
    resource_type = models.CharField(max_length=50, blank=True, null=True)
    latest = models.IntegerField(blank=True, null=True)
    ref_id = models.CharField(max_length=50, blank=True, null=True)
    attach_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_metadata'


class FileModule(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pos = models.FloatField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    module_type = models.CharField(max_length=20, blank=True, null=True)
    repository_path = models.CharField(max_length=255, blank=True, null=True)
    repository_user_name = models.CharField(max_length=255, blank=True, null=True)
    repository_token = models.CharField(max_length=255, blank=True, null=True)
    repository_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_module'


class FunctionCaseExecutionInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    source_id = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'function_case_execution_info'


class Group(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=100, blank=True, null=True)
    system = models.IntegerField()
    type = models.CharField(max_length=20)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    creator = models.CharField(max_length=64)
    scope_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'group'


class IssueComment(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    issue_id = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_comment'


class IssueFollow(models.Model):
    issue_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_follow'
        unique_together = (('issue_id', 'follow_id'),)


class IssueTemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=64)
    platform = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    system = models.IntegerField(blank=True, null=True)
    global_field = models.IntegerField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    content = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_template'


class Issues(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    reporter = models.CharField(max_length=50, blank=True, null=True)
    lastmodify = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50)
    custom_fields = models.TextField(blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)
    resource_id = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    platform_status = models.CharField(max_length=50, blank=True, null=True)
    platform_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'issues'


class JarConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=64)
    file_name = models.CharField(max_length=64)
    creator = models.CharField(max_length=50)
    modifier = models.CharField(max_length=50)
    path = models.CharField(max_length=255)
    enable = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    resource_id = models.CharField(max_length=50)
    resource_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'jar_config'


class License(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    license_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license'


class LoadTest(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    load_configuration = models.TextField(blank=True, null=True)
    advanced_configuration = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    status = models.CharField(max_length=64, blank=True, null=True)
    test_resource_pool_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    scenario_version = models.IntegerField(blank=True, null=True)
    scenario_id = models.CharField(max_length=255, blank=True, null=True)
    order = models.BigIntegerField()
    version_id = models.CharField(max_length=50, blank=True, null=True)
    ref_id = models.CharField(max_length=50, blank=True, null=True)
    latest = models.IntegerField(blank=True, null=True)
    env_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test'


class LoadTestFile(models.Model):
    test_id = models.CharField(max_length=64, blank=True, null=True)
    file_id = models.CharField(max_length=64, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_file'
        unique_together = (('test_id', 'file_id'),)


class LoadTestFollow(models.Model):
    test_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_follow'
        unique_together = (('test_id', 'follow_id'),)


class LoadTestReport(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    status = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    trigger_mode = models.CharField(max_length=64, blank=True, null=True)
    load_configuration = models.TextField(blank=True, null=True)
    file_id = models.CharField(max_length=50, blank=True, null=True)
    max_users = models.CharField(max_length=10, blank=True, null=True)
    avg_response_time = models.CharField(max_length=10, blank=True, null=True)
    tps = models.CharField(max_length=10, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    test_name = models.CharField(max_length=255, blank=True, null=True)
    jmx_content = models.TextField(blank=True, null=True)
    advanced_configuration = models.TextField(blank=True, null=True)
    test_resource_pool_id = models.CharField(max_length=50, blank=True, null=True)
    test_start_time = models.BigIntegerField(blank=True, null=True)
    test_end_time = models.BigIntegerField(blank=True, null=True)
    test_duration = models.BigIntegerField(blank=True, null=True)
    version_id = models.CharField(max_length=50, blank=True, null=True)
    env_info = models.TextField(blank=True, null=True)
    relevance_test_plan_report_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_report'


class LoadTestReportDetail(models.Model):
    part = models.BigAutoField(primary_key=True)
    report_id = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_report_detail'
        unique_together = (('part', 'report_id'),)


class LoadTestReportFile(models.Model):
    report_id = models.CharField(max_length=50, db_collation='utf8mb4_bin', blank=True, null=True)
    file_id = models.CharField(max_length=50, db_collation='utf8mb4_bin', blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_report_file'
        unique_together = (('report_id', 'file_id'),)


class LoadTestReportLog(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    report_id = models.CharField(max_length=50)
    resource_id = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    part = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_report_log'


class LoadTestReportResult(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    report_id = models.CharField(max_length=50)
    report_key = models.CharField(max_length=64, blank=True, null=True)
    report_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_report_result'


class LoadTestReportResultPart(models.Model):
    report_id = models.CharField(primary_key=True, max_length=50)
    report_key = models.CharField(max_length=64)
    resource_index = models.IntegerField()
    report_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_report_result_part'
        unique_together = (('report_id', 'report_key', 'resource_index'),)


class LoadTestReportResultRealtime(models.Model):
    report_id = models.CharField(primary_key=True, max_length=50)
    report_key = models.CharField(max_length=64)
    resource_index = models.IntegerField()
    sort = models.IntegerField()
    report_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'load_test_report_result_realtime'
        unique_together = (('report_id', 'report_key', 'resource_index', 'sort'),)


class MessageTask(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    type = models.CharField(max_length=50)
    event = models.CharField(max_length=255)
    user_id = models.CharField(max_length=50)
    task_type = models.CharField(max_length=64)
    webhook = models.CharField(max_length=255, blank=True, null=True)
    identification = models.CharField(max_length=50)
    is_set = models.IntegerField()
    test_id = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    project_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_task'


class MetersphereVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'metersphere_version'


class MinderExtraNode(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    parent_id = models.CharField(max_length=50)
    group_id = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    node_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minder_extra_node'


class MockConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    api_id = models.CharField(max_length=50)
    api_path = models.CharField(max_length=1000, blank=True, null=True)
    api_method = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    create_user_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mock_config'


class MockExpectConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    mock_config_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    create_user_id = models.CharField(max_length=64, blank=True, null=True)
    expect_num = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mock_expect_config'


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    receiver = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    operation = models.CharField(max_length=50, blank=True, null=True)
    resource_id = models.CharField(max_length=50, blank=True, null=True)
    resource_type = models.CharField(max_length=50, blank=True, null=True)
    resource_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'


class OperatingLog(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    oper_method = models.CharField(max_length=500, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    oper_user = models.CharField(max_length=50, blank=True, null=True)
    source_id = models.CharField(max_length=6000, blank=True, null=True)
    oper_type = models.CharField(max_length=100, blank=True, null=True)
    oper_module = models.CharField(max_length=100, blank=True, null=True)
    oper_title = models.CharField(max_length=6000, blank=True, null=True)
    oper_path = models.CharField(max_length=500, blank=True, null=True)
    oper_content = models.TextField(blank=True, null=True)
    oper_params = models.TextField(blank=True, null=True)
    oper_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'operating_log'


class OperatingLogResource(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    operating_log_id = models.CharField(max_length=50)
    source_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'operating_log_resource'


class Organization(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'


class PerformanceVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'performance_version'


class Plugin(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=300, blank=True, null=True)
    plugin_id = models.CharField(max_length=300)
    script_id = models.CharField(max_length=300)
    clazz_name = models.CharField(max_length=500)
    jmeter_clazz = models.CharField(max_length=300)
    source_path = models.CharField(max_length=300)
    source_name = models.CharField(max_length=300)
    form_option = models.TextField(blank=True, null=True)
    form_script = models.TextField(blank=True, null=True)
    exec_entry = models.CharField(max_length=300, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    create_user_id = models.CharField(max_length=64, blank=True, null=True)
    xpack = models.IntegerField(blank=True, null=True)
    scenario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'plugin'


class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    workspace_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    tapd_id = models.CharField(max_length=50, blank=True, null=True)
    jira_key = models.CharField(max_length=50, blank=True, null=True)
    zentao_id = models.CharField(max_length=50, blank=True, null=True)
    azure_devops_id = models.CharField(max_length=50, blank=True, null=True)
    case_template_id = models.CharField(max_length=50, blank=True, null=True)
    issue_template_id = models.CharField(max_length=50, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    system_id = models.CharField(max_length=50, blank=True, null=True)
    azure_filter_id = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=20)
    third_part_template = models.IntegerField(blank=True, null=True)
    version_enable = models.IntegerField(blank=True, null=True)
    issue_config = models.TextField(blank=True, null=True)
    api_template_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectApplication(models.Model):
    project_id = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    type_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_application'
        unique_together = (('project_id', 'type'),)


class ProjectManagementVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_management_version'


class ProjectVersion(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    latest = models.IntegerField(blank=True, null=True)
    publish_time = models.BigIntegerField(blank=True, null=True)
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_version'


class QrtzBlobTriggers(models.Model):
    sched_name = models.OneToOneField('QrtzTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True)  # Field name made lowercase.
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='qbt_trigger_names')  # Field name made lowercase.
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='qbt_trigger_groups')  # Field name made lowercase.
    blob_data = models.TextField(db_column='BLOB_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_blob_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzCalendars(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    calendar_name = models.CharField(db_column='CALENDAR_NAME', max_length=200)  # Field name made lowercase.
    calendar = models.TextField(db_column='CALENDAR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_calendars'
        unique_together = (('sched_name', 'calendar_name'),)


class QrtzCronTriggers(models.Model):
    sched_name = models.OneToOneField('QrtzTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True)  # Field name made lowercase.
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='qct_trigger_names')  # Field name made lowercase.
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='qct_trigger_groups')  # Field name made lowercase.
    cron_expression = models.CharField(db_column='CRON_EXPRESSION', max_length=120)  # Field name made lowercase.
    time_zone_id = models.CharField(db_column='TIME_ZONE_ID', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_cron_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzFiredTriggers(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    entry_id = models.CharField(db_column='ENTRY_ID', max_length=95)  # Field name made lowercase.
    trigger_name = models.CharField(db_column='TRIGGER_NAME', max_length=200)  # Field name made lowercase.
    trigger_group = models.CharField(db_column='TRIGGER_GROUP', max_length=200)  # Field name made lowercase.
    instance_name = models.CharField(db_column='INSTANCE_NAME', max_length=200)  # Field name made lowercase.
    fired_time = models.BigIntegerField(db_column='FIRED_TIME')  # Field name made lowercase.
    sched_time = models.BigIntegerField(db_column='SCHED_TIME')  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY')  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=16)  # Field name made lowercase.
    job_name = models.CharField(db_column='JOB_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job_group = models.CharField(db_column='JOB_GROUP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_nonconcurrent = models.CharField(db_column='IS_NONCONCURRENT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    requests_recovery = models.CharField(db_column='REQUESTS_RECOVERY', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_fired_triggers'
        unique_together = (('sched_name', 'entry_id'),)


class QrtzJobDetails(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    job_name = models.CharField(db_column='JOB_NAME', max_length=200)  # Field name made lowercase.
    job_group = models.CharField(db_column='JOB_GROUP', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    job_class_name = models.CharField(db_column='JOB_CLASS_NAME', max_length=250)  # Field name made lowercase.
    is_durable = models.CharField(db_column='IS_DURABLE', max_length=1)  # Field name made lowercase.
    is_nonconcurrent = models.CharField(db_column='IS_NONCONCURRENT', max_length=1)  # Field name made lowercase.
    is_update_data = models.CharField(db_column='IS_UPDATE_DATA', max_length=1)  # Field name made lowercase.
    requests_recovery = models.CharField(db_column='REQUESTS_RECOVERY', max_length=1)  # Field name made lowercase.
    job_data = models.TextField(db_column='JOB_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_job_details'
        unique_together = (('sched_name', 'job_name', 'job_group'),)


class QrtzLocks(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    lock_name = models.CharField(db_column='LOCK_NAME', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_locks'
        unique_together = (('sched_name', 'lock_name'),)


class QrtzPausedTriggerGrps(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    trigger_group = models.CharField(db_column='TRIGGER_GROUP', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_paused_trigger_grps'
        unique_together = (('sched_name', 'trigger_group'),)


class QrtzSchedulerState(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    instance_name = models.CharField(db_column='INSTANCE_NAME', max_length=200)  # Field name made lowercase.
    last_checkin_time = models.BigIntegerField(db_column='LAST_CHECKIN_TIME')  # Field name made lowercase.
    checkin_interval = models.BigIntegerField(db_column='CHECKIN_INTERVAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_scheduler_state'
        unique_together = (('sched_name', 'instance_name'),)


class QrtzSimpleTriggers(models.Model):
    sched_name = models.OneToOneField('QrtzTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True)  # Field name made lowercase.
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='qst_trigger_names')  # Field name made lowercase.
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='qst_trigger_groups')  # Field name made lowercase.
    repeat_count = models.BigIntegerField(db_column='REPEAT_COUNT')  # Field name made lowercase.
    repeat_interval = models.BigIntegerField(db_column='REPEAT_INTERVAL')  # Field name made lowercase.
    times_triggered = models.BigIntegerField(db_column='TIMES_TRIGGERED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_simple_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzSimpropTriggers(models.Model):
    sched_name = models.OneToOneField('QrtzTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True)  # Field name made lowercase.
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='qspt_trigger_names')  # Field name made lowercase.
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='qspt_trigger_groups')  # Field name made lowercase.
    str_prop_1 = models.CharField(db_column='STR_PROP_1', max_length=512, blank=True, null=True)  # Field name made lowercase.
    str_prop_2 = models.CharField(db_column='STR_PROP_2', max_length=512, blank=True, null=True)  # Field name made lowercase.
    str_prop_3 = models.CharField(db_column='STR_PROP_3', max_length=512, blank=True, null=True)  # Field name made lowercase.
    int_prop_1 = models.IntegerField(db_column='INT_PROP_1', blank=True, null=True)  # Field name made lowercase.
    int_prop_2 = models.IntegerField(db_column='INT_PROP_2', blank=True, null=True)  # Field name made lowercase.
    long_prop_1 = models.BigIntegerField(db_column='LONG_PROP_1', blank=True, null=True)  # Field name made lowercase.
    long_prop_2 = models.BigIntegerField(db_column='LONG_PROP_2', blank=True, null=True)  # Field name made lowercase.
    dec_prop_1 = models.DecimalField(db_column='DEC_PROP_1', max_digits=13, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dec_prop_2 = models.DecimalField(db_column='DEC_PROP_2', max_digits=13, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bool_prop_1 = models.CharField(db_column='BOOL_PROP_1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bool_prop_2 = models.CharField(db_column='BOOL_PROP_2', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_simprop_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzTriggers(models.Model):
    sched_name = models.OneToOneField(QrtzJobDetails, models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True)  # Field name made lowercase.
    trigger_name = models.CharField(db_column='TRIGGER_NAME', max_length=200)  # Field name made lowercase.
    trigger_group = models.CharField(db_column='TRIGGER_GROUP', max_length=200)  # Field name made lowercase.
    job_name = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='JOB_NAME', related_name='qt_job_names')  # Field name made lowercase.
    job_group = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='JOB_GROUP', related_name='qt_job_groups')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    next_fire_time = models.BigIntegerField(db_column='NEXT_FIRE_TIME', blank=True, null=True)  # Field name made lowercase.
    prev_fire_time = models.BigIntegerField(db_column='PREV_FIRE_TIME', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    trigger_state = models.CharField(db_column='TRIGGER_STATE', max_length=16)  # Field name made lowercase.
    trigger_type = models.CharField(db_column='TRIGGER_TYPE', max_length=8)  # Field name made lowercase.
    start_time = models.BigIntegerField(db_column='START_TIME')  # Field name made lowercase.
    end_time = models.BigIntegerField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    calendar_name = models.CharField(db_column='CALENDAR_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    misfire_instr = models.SmallIntegerField(db_column='MISFIRE_INSTR', blank=True, null=True)  # Field name made lowercase.
    job_data = models.TextField(db_column='JOB_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrtz_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class Quota(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    api = models.IntegerField(blank=True, null=True)
    performance = models.IntegerField(blank=True, null=True)
    max_threads = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    resource_pool = models.CharField(max_length=1000, blank=True, null=True)
    workspace_id = models.CharField(max_length=50, blank=True, null=True)
    use_default = models.IntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    member = models.IntegerField(blank=True, null=True)
    project = models.IntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    vum_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vum_used = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quota'


class RelationshipEdge(models.Model):
    source_id = models.CharField(primary_key=True, max_length=50)
    target_id = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    graph_id = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'relationship_edge'
        unique_together = (('source_id', 'target_id'),)


class ReportStatistics(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    update_user = models.CharField(max_length=64, blank=True, null=True)
    select_option = models.TextField(blank=True, null=True)
    data_option = models.TextField(blank=True, null=True)
    report_type = models.CharField(max_length=50)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_statistics'


class ReportVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report_version'


class Role(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'role'


class ScenarioExecutionInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    source_id = models.CharField(max_length=255)
    result = models.CharField(max_length=50)
    trigger_mode = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField()
    project_id = models.CharField(max_length=50, blank=True, null=True)
    execute_type = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario_execution_info'


class Schedule(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    key = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=255)
    group = models.CharField(max_length=50, blank=True, null=True)
    job = models.CharField(max_length=64)
    enable = models.IntegerField(blank=True, null=True)
    resource_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=50)
    workspace_id = models.CharField(max_length=50)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    config = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class ServiceIntegration(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    platform = models.CharField(max_length=50)
    configuration = models.TextField()
    workspace_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_integration'


class ShareInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    create_time = models.BigIntegerField()
    create_user_id = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.BigIntegerField()
    share_type = models.CharField(max_length=64, blank=True, null=True)
    custom_data = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'share_info'


class SwaggerUrlProject(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    project_id = models.CharField(max_length=120, blank=True, null=True)
    swagger_url = models.CharField(max_length=255, blank=True, null=True)
    module_id = models.CharField(max_length=120, blank=True, null=True)
    module_path = models.CharField(max_length=255, blank=True, null=True)
    mode_id = models.CharField(max_length=120, blank=True, null=True)
    config = models.TextField(blank=True, null=True)
    cover_module = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swagger_url_project'


class SystemHeader(models.Model):
    type = models.CharField(primary_key=True, max_length=150)
    props = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_header'


class SystemParameter(models.Model):
    param_key = models.CharField(primary_key=True, max_length=64)
    param_value = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_parameter'


class TestCase(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    node_id = models.CharField(max_length=50)
    test_id = models.CharField(max_length=2000, blank=True, null=True)
    node_path = models.CharField(max_length=999)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=25, blank=True, null=True)
    maintainer = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    method = models.CharField(max_length=15, blank=True, null=True)
    prerequisite = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    steps = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    sort = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    review_status = models.CharField(max_length=25, blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    demand_id = models.CharField(max_length=120, blank=True, null=True)
    demand_name = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    step_description = models.TextField(blank=True, null=True)
    expected_result = models.TextField(blank=True, null=True)
    custom_fields = models.TextField(blank=True, null=True)
    step_model = models.CharField(max_length=10, blank=True, null=True)
    custom_num = models.CharField(max_length=64, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    original_status = models.CharField(max_length=50, blank=True, null=True)
    delete_time = models.BigIntegerField(blank=True, null=True)
    delete_user_id = models.CharField(max_length=64, blank=True, null=True)
    order = models.BigIntegerField()
    case_public = models.IntegerField(blank=True, null=True)
    version_id = models.CharField(max_length=50, blank=True, null=True)
    ref_id = models.CharField(max_length=50, blank=True, null=True)
    latest = models.IntegerField(blank=True, null=True)
    last_execute_result = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case'


class TestCaseComment(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    case_id = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=80, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_comment'


class TestCaseFile(models.Model):
    case_id = models.CharField(max_length=64, blank=True, null=True)
    file_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_file'
        unique_together = (('case_id', 'file_id'),)


class TestCaseFollow(models.Model):
    case_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_follow'
        unique_together = (('case_id', 'follow_id'),)


class TestCaseIssues(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    resource_id = models.CharField(max_length=50)
    issues_id = models.CharField(max_length=100)
    ref_type = models.CharField(max_length=30)
    ref_id = models.CharField(max_length=50, blank=True, null=True)
    relate_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_issues'


class TestCaseNode(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pos = models.FloatField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_node'


class TestCaseReport(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=64)
    content = models.TextField(blank=True, null=True)
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_report'


class TestCaseReportTemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=64)
    workspace_id = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_report_template'


class TestCaseReview(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=200, blank=True, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=2000, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review'


class TestCaseReviewApiCase(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_case_review_id = models.CharField(max_length=50, blank=True, null=True)
    api_case_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    environment_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review_api_case'


class TestCaseReviewFollow(models.Model):
    review_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review_follow'
        unique_together = (('review_id', 'follow_id'),)


class TestCaseReviewLoad(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_case_review_id = models.CharField(max_length=50, blank=True, null=True)
    load_case_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    load_report_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review_load'


class TestCaseReviewProject(models.Model):
    review_id = models.CharField(max_length=50, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review_project'
        unique_together = (('review_id', 'project_id'),)


class TestCaseReviewScenario(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_case_review_id = models.CharField(max_length=50, blank=True, null=True)
    api_scenario_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    pass_rate = models.CharField(max_length=100, blank=True, null=True)
    last_result = models.CharField(max_length=100, blank=True, null=True)
    report_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review_scenario'


class TestCaseReviewTestCase(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    review_id = models.CharField(max_length=64, blank=True, null=True)
    case_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    reviewer = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    order = models.BigIntegerField()
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review_test_case'


class TestCaseReviewUsers(models.Model):
    review_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_review_users'
        unique_together = (('review_id', 'user_id'),)


class TestCaseTemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, null=True)
    case_name = models.CharField(max_length=64, blank=True, null=True)
    system = models.IntegerField(blank=True, null=True)
    global_field = models.IntegerField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    prerequisite = models.TextField(blank=True, null=True)
    step_description = models.TextField(blank=True, null=True)
    expected_result = models.TextField(blank=True, null=True)
    actual_result = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    step_model = models.CharField(max_length=10, blank=True, null=True)
    steps = models.TextField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_template'


class TestCaseTest(models.Model):
    test_case_id = models.CharField(max_length=50, blank=True, null=True)
    test_id = models.CharField(max_length=50, blank=True, null=True)
    test_type = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    update_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_test'
        unique_together = (('test_case_id', 'test_id'),)


class TestPlan(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    workspace_id = models.CharField(max_length=50)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20)
    stage = models.CharField(max_length=30)
    tags = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    planned_start_time = models.BigIntegerField(blank=True, null=True)
    planned_end_time = models.BigIntegerField(blank=True, null=True)
    actual_start_time = models.BigIntegerField(blank=True, null=True)
    actual_end_time = models.BigIntegerField(blank=True, null=True)
    creator = models.CharField(max_length=255)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    execution_times = models.IntegerField(blank=True, null=True)
    automatic_status_update = models.IntegerField(blank=True, null=True)
    report_summary = models.TextField(blank=True, null=True)
    report_config = models.TextField(blank=True, null=True)
    repeat_case = models.IntegerField(blank=True, null=True)
    run_mode_config = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan'


class TestPlanApiCase(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_plan_id = models.CharField(max_length=50)
    api_case_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50, blank=True, null=True)
    environment_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)
    order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'test_plan_api_case'


class TestPlanApiScenario(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_plan_id = models.CharField(max_length=50)
    api_scenario_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pass_rate = models.CharField(max_length=100, blank=True, null=True)
    last_result = models.CharField(max_length=100, blank=True, null=True)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    order = models.BigIntegerField()
    environment_type = models.CharField(max_length=20, blank=True, null=True)
    environment_group_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_api_scenario'


class TestPlanExecutionQueue(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    report_id = models.CharField(max_length=100, blank=True, null=True)
    run_mode = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    test_plan_id = models.CharField(max_length=100, blank=True, null=True)
    resource_id = models.CharField(max_length=100, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_execution_queue'


class TestPlanFollow(models.Model):
    test_plan_id = models.CharField(max_length=50, blank=True, null=True)
    follow_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_follow'
        unique_together = (('test_plan_id', 'follow_id'),)


class TestPlanLoadCase(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_plan_id = models.CharField(max_length=50)
    load_case_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50, blank=True, null=True)
    load_report_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)
    test_resource_pool_id = models.CharField(max_length=50, blank=True, null=True)
    load_configuration = models.TextField(blank=True, null=True)
    order = models.BigIntegerField()
    advanced_configuration = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_load_case'


class TestPlanPrincipal(models.Model):
    test_plan_id = models.CharField(max_length=50, blank=True, null=True)
    principal_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_principal'
        unique_together = (('test_plan_id', 'principal_id'),)


class TestPlanProject(models.Model):
    test_plan_id = models.CharField(max_length=50, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_project'
        unique_together = (('test_plan_id', 'project_id'),)


class TestPlanReport(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_plan_id = models.CharField(max_length=50)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    name = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    trigger_mode = models.CharField(max_length=50, blank=True, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    is_api_case_executing = models.IntegerField(blank=True, null=True)
    is_scenario_executing = models.IntegerField(blank=True, null=True)
    is_ui_scenario_executing = models.IntegerField(blank=True, null=True)
    is_performance_executing = models.IntegerField(blank=True, null=True)
    principal = models.CharField(max_length=50, blank=True, null=True)
    components = models.CharField(max_length=20, blank=True, null=True)
    is_new = models.IntegerField(blank=True, null=True)
    run_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_report'
        unique_together = (('test_plan_id', 'create_time'),)


class TestPlanReportContent(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_plan_report_id = models.CharField(unique=True, max_length=50)
    start_time = models.BigIntegerField(blank=True, null=True)
    case_count = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    execute_rate = models.FloatField(blank=True, null=True)
    pass_rate = models.FloatField(blank=True, null=True)
    is_third_part_issue = models.IntegerField(blank=True, null=True)
    config = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    function_result = models.TextField(blank=True, null=True)
    api_result = models.TextField(blank=True, null=True)
    load_result = models.TextField(blank=True, null=True)
    function_all_cases = models.TextField(blank=True, null=True)
    function_failure_cases = models.TextField(blank=True, null=True)
    issue_list = models.TextField(blank=True, null=True)
    api_all_cases = models.TextField(blank=True, null=True)
    api_failure_cases = models.TextField(blank=True, null=True)
    scenario_all_cases = models.TextField(blank=True, null=True)
    scenario_failure_cases = models.TextField(blank=True, null=True)
    load_all_cases = models.TextField(db_column='load_all_Cases', blank=True, null=True)  # Field name made lowercase.
    load_failure_cases = models.TextField(blank=True, null=True)
    plan_scenario_report_struct = models.TextField(blank=True, null=True)
    plan_api_case_report_struct = models.TextField(blank=True, null=True)
    plan_load_case_report_struct = models.TextField(blank=True, null=True)
    error_report_cases = models.TextField(blank=True, null=True)
    error_report_scenarios = models.TextField(blank=True, null=True)
    un_execute_cases = models.TextField(blank=True, null=True)
    un_execute_scenarios = models.TextField(blank=True, null=True)
    api_base_count = models.TextField(blank=True, null=True)
    plan_ui_scenario_report_struct = models.TextField(blank=True, null=True)
    ui_result = models.TextField(blank=True, null=True)
    ui_all_cases = models.TextField(blank=True, null=True)
    ui_failure_cases = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_report_content'


class TestPlanReportData(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_plan_report_id = models.CharField(unique=True, max_length=50)
    execute_result = models.TextField(blank=True, null=True)
    failur_test_cases = models.TextField(blank=True, null=True)
    module_execute_result = models.TextField(blank=True, null=True)
    api_case_info = models.TextField(blank=True, null=True)
    scenario_info = models.TextField(blank=True, null=True)
    performance_info = models.TextField(blank=True, null=True)
    issues_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_report_data'


class TestPlanTestCase(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    plan_id = models.CharField(max_length=50)
    case_id = models.CharField(max_length=50)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    executor = models.CharField(max_length=64)
    status = models.CharField(max_length=15, blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    issues = models.TextField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    actual_result = models.TextField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    issues_count = models.IntegerField(blank=True, null=True)
    order = models.BigIntegerField()
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_test_case'


class TestPlanUiScenario(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_plan_id = models.CharField(max_length=50)
    ui_scenario_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pass_rate = models.CharField(max_length=100, blank=True, null=True)
    last_result = models.CharField(max_length=100, blank=True, null=True)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    order = models.BigIntegerField()
    environment_type = models.CharField(max_length=20, blank=True, null=True)
    environment_group_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_plan_ui_scenario'


class TestResource(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    test_resource_pool_id = models.CharField(max_length=50)
    configuration = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=64)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'test_resource'


class TestResourcePool(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=64)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    image = models.CharField(max_length=100, blank=True, null=True)
    heap = models.CharField(max_length=200, blank=True, null=True)
    gc_algo = models.CharField(max_length=200, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    api = models.IntegerField(blank=True, null=True)
    performance = models.IntegerField(blank=True, null=True)
    backend_listener = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_resource_pool'


class TrackVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'track_version'


class UiElement(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    num = models.IntegerField(blank=True, null=True)
    module_id = models.CharField(max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    location_type = models.CharField(max_length=30)
    location = models.CharField(max_length=300)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100)
    version_id = models.CharField(max_length=50)
    ref_id = models.CharField(max_length=50)
    order = models.BigIntegerField()
    latest = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ui_element'


class UiElementModule(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    module_path = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pos = models.FloatField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ui_element_module'


class UiElementReference(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    element_id = models.CharField(max_length=255, blank=True, null=True)
    element_module_id = models.CharField(max_length=255, blank=True, null=True)
    scenario_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=50)
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ui_element_reference'


class UiScenario(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    project_id = models.CharField(max_length=50)
    tags = models.CharField(max_length=2000, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    module_id = models.CharField(max_length=64, blank=True, null=True)
    module_path = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=100, blank=True, null=True)
    scenario_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    step_total = models.IntegerField(blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    scenario_definition = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pass_rate = models.CharField(max_length=100, blank=True, null=True)
    last_result = models.CharField(max_length=100, blank=True, null=True)
    report_id = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    original_state = models.CharField(max_length=64, blank=True, null=True)
    custom_num = models.CharField(max_length=64, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    use_url = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    delete_time = models.BigIntegerField(blank=True, null=True)
    delete_user_id = models.CharField(max_length=64, blank=True, null=True)
    execute_times = models.IntegerField(blank=True, null=True)
    order = models.BigIntegerField()
    environment_type = models.CharField(max_length=20, blank=True, null=True)
    environment_json = models.TextField(blank=True, null=True)
    environment_group_id = models.CharField(max_length=50, blank=True, null=True)
    version_id = models.CharField(max_length=50)
    ref_id = models.CharField(max_length=255)
    latest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ui_scenario'


class UiScenarioModule(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    module_path = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    scenario_type = models.CharField(max_length=100)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    pos = models.FloatField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ui_scenario_module'


class UiScenarioReference(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    ui_scenario_id = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    create_user_id = models.CharField(max_length=64, blank=True, null=True)
    reference_id = models.CharField(max_length=255, blank=True, null=True)
    reference_type = models.CharField(max_length=255, blank=True, null=True)
    data_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ui_scenario_reference'


class UiTaskRefresh(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    task_key = models.CharField(max_length=255, blank=True, null=True)
    task_status = models.IntegerField(blank=True, null=True)
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ui_task_refresh'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=50, db_collation='utf8mb4_bin')
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=256, db_collation='utf8mb4_bin', blank=True, null=True)
    status = models.CharField(max_length=50)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    language = models.CharField(max_length=30, blank=True, null=True)
    last_workspace_id = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    last_project_id = models.CharField(max_length=50, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    platform_info = models.TextField(blank=True, null=True)
    selenium_server = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    user_id = models.CharField(max_length=64)
    group_id = models.CharField(max_length=64)
    source_id = models.CharField(max_length=64)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_group'


class UserGroupPermission(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    group_id = models.CharField(max_length=64)
    permission_id = models.CharField(max_length=128)
    module_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user_group_permission'


class UserHeader(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    props = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_header'


class UserKey(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=50)
    access_key = models.CharField(unique=True, max_length=50)
    secret_key = models.CharField(max_length=50)
    create_time = models.BigIntegerField()
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_key'


class UserRole(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=50)
    role_id = models.CharField(max_length=50)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_role'


class Workspace(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.BigIntegerField()
    create_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workspace'
