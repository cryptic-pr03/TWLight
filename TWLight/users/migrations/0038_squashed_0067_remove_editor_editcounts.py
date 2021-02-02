# Generated by Django 3.0.11 on 2021-02-02 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

# TWLight.users.migrations.0053_twl_team_user
# data migration, should come after all userprofile migrations.
def twl_team(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    User.objects.get_or_create(
        username="TWL Team", email="wikipedialibrary@wikimedia.org"
    )


# TWLight.users.migrations.0055_authorization_data_partners_foreignkey_to_manytomany
# data migration, may be skipped.

# TWLight.users.migrations.0057_expire_all_sessions
# data migration, may be skipped.

# TWLight.users.migrations.0061_make_staff_superusers_wp_eligible
# data migration, may be skipped.

# TWLight.users.migrations.0062_delete_hanging_userless_bundle_auths
# data migration, may be skipped.

# TWLight.users.migrations.0063_check_terms_and_bundle_eligibility
# data migration, may be skipped.

# TWLight.users.migrations.0066_move_editcounts_to_log
# data migration, may be skipped.


class Migration(migrations.Migration):

    replaces = [
        ("users", "0038_auto_20190220_1639"),
        ("users", "0039_auto_20190423_0953"),
        ("users", "0040_auto_20190509_1546"),
        ("users", "0041_auto_20190523_1250"),
        ("users", "0042_auto_20190530_1757"),
        ("users", "0043_auto_20190628_1551"),
        ("users", "0044_auto_20190801_1703"),
        ("users", "0045_auto_20190808_1849"),
        ("users", "0046_auto_20191001_1455"),
        ("users", "0047_auto_20191017_0459"),
        ("users", "0048_reset_tou_for_all_users"),
        ("users", "0049_auto_20191216_1742"),
        ("users", "0050_auto_20200109_1642"),
        ("users", "0051_userprofile_proxy_notification_sent"),
        ("users", "0052_auto_20200312_1628"),
        ("users", "0053_twl_team_user"),
        ("users", "0054_auto_20200508_1715"),
        ("users", "0055_authorization_data_partners_foreignkey_to_manytomany"),
        ("users", "0056_remove_authorization_partner"),
        ("users", "0057_expire_all_sessions"),
        ("users", "0058_auto_20200615_2030"),
        ("users", "0059_auto_20200706_1659"),
        ("users", "0060_auto_20200804_1634"),
        ("users", "0061_make_staff_superusers_wp_eligible"),
        ("users", "0062_delete_hanging_userless_bundle_auths"),
        ("users", "0063_check_terms_and_bundle_eligibility"),
        ("users", "0064_auto_20201019_1310"),
        ("users", "0065_editorlog"),
        ("users", "0066_move_editcounts_to_log"),
        ("users", "0067_remove_editor_editcounts"),
    ]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("resources", "0001_initial_squashed_0062_auto_20190220_1639"),
        ("users", "0001_squashed_0037_auto_20190117_1008"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="editor",
            name="wp_editcount",
        ),
        migrations.AddField(
            model_name="editor",
            name="ignore_wp_blocks",
            field=models.BooleanField(
                default=False,
                help_text="Ignore the 'not currently blocked' criterion for access?",
            ),
        ),
        migrations.AddField(
            model_name="editor",
            name="wp_account_old_enough",
            field=models.BooleanField(
                default=False,
                editable=False,
                help_text="At their last login, did this user meet the account age criterion in the terms of use?",
            ),
        ),
        migrations.AddField(
            model_name="editor",
            name="wp_bundle_eligible",
            field=models.BooleanField(
                default=False,
                editable=False,
                help_text="At their last login, did this user meet the criteria for access to the library card bundle?",
            ),
        ),
        migrations.AddField(
            model_name="editor",
            name="wp_enough_edits",
            field=models.BooleanField(
                default=False,
                editable=False,
                help_text="At their last login, did this user meet the total editcount criterion in the terms of use?",
            ),
        ),
        migrations.AddField(
            model_name="editor",
            name="wp_enough_recent_edits",
            field=models.BooleanField(
                default=False,
                editable=False,
                help_text="At their last login, did this user meet the recent editcount criterion in the terms of use?",
            ),
        ),
        migrations.AddField(
            model_name="editor",
            name="wp_not_blocked",
            field=models.BooleanField(
                default=False,
                editable=False,
                help_text="At their last login, did this user meet the 'not currently blocked' criterion in the terms of use?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="approved_app_reminders",
            field=models.BooleanField(
                default=True,
                help_text="Does this coordinator want approved app reminder notices?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="discussion_app_reminders",
            field=models.BooleanField(
                default=True,
                help_text="Does this coordinator want under discussion app reminder notices?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="pending_app_reminders",
            field=models.BooleanField(
                default=True,
                help_text="Does this coordinator want pending app reminder notices?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="proxy_notification_sent",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="send_renewal_notices",
            field=models.BooleanField(
                default=True, help_text="Does this user want renewal reminder notices?"
            ),
        ),
        migrations.AlterField(
            model_name="editor",
            name="wp_valid",
            field=models.BooleanField(
                default=False,
                editable=False,
                help_text="At their last login, did this user meet the criteria in the terms of use?",
            ),
        ),
        migrations.RunPython(twl_team, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="userprofile",
            name="lang",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ar", "العربية"),
                    ("br", "brezhoneg"),
                    ("da", "dansk"),
                    ("de", "Deutsch"),
                    ("en", "English"),
                    ("en-gb", "British English"),
                    ("eo", "Esperanto"),
                    ("es", "español"),
                    ("fa", "فارسی"),
                    ("fi", "suomi"),
                    ("fr", "français"),
                    ("hi", "हिन्दी"),
                    ("id", "Bahasa Indonesia"),
                    ("ja", "日本語"),
                    ("ko", "한국어"),
                    ("mk", "македонски"),
                    ("mr", "मराठी"),
                    ("my", "မြန်မာဘာသာ"),
                    ("pl", "polski"),
                    ("pt", "português"),
                    ("pt-br", "português do Brasil"),
                    ("ro", "română"),
                    ("ru", "русский"),
                    ("sv", "svenska"),
                    ("ta", "தமிழ்"),
                    ("tr", "Türkçe"),
                    ("uk", "українська"),
                    ("vi", "Tiếng Việt"),
                    ("zh-hans", "中文（简体）"),
                    ("zh-hant", "中文（繁體）"),
                ],
                help_text="Language",
                max_length=128,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="EditorLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "editcount",
                    models.IntegerField(
                        default=None, editable=False, help_text="Wikipedia edit count"
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        db_index=True,
                        default=None,
                        editable=False,
                        help_text="When the editcount was updated from Wikipedia",
                    ),
                ),
                (
                    "editor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="editorlogs",
                        to="users.Editor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Authorization",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_authorized", models.DateField(auto_now_add=True)),
                (
                    "date_expires",
                    models.DateField(
                        blank=True,
                        help_text="The date this authorization expires.",
                        null=True,
                    ),
                ),
                (
                    "reminder_email_sent",
                    models.BooleanField(
                        default=False,
                        help_text="Have we sent a reminder email about this authorization?",
                    ),
                ),
                (
                    "authorizer",
                    models.ForeignKey(
                        help_text="The authorizing user.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The authorized user.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="authorizations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "partners",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The partner(s) for which the editor is authorized.",
                        limit_choices_to=models.Q(status__in=[0, 2]),
                        to="resources.Partner",
                    ),
                ),
                (
                    "stream",
                    models.ForeignKey(
                        blank=True,
                        help_text="The stream for which the editor is authorized.",
                        limit_choices_to=models.Q(partner__status__in=[0, 2]),
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="resources.Stream",
                    ),
                ),
            ],
            options={
                "verbose_name": "authorization",
                "verbose_name_plural": "authorizations",
            },
        ),
    ]
