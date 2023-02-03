# Generated by Django 4.1.5 on 2023-02-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "aft_payment",
            "0003_alter_b2centries_status_alter_b2crecipient_reason_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="b2centries",
            name="status",
            field=models.CharField(
                choices=[
                    ("Failed", "Failed"),
                    ("NotSupported", "NotSupported"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="b2crecipient",
            name="reason",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "BusinessPaymentWithWithdrawalChargePaid",
                        "BusinessPaymentWithWithdrawalChargePaid",
                    ),
                    (
                        "SalaryPaymentWithWithdrawalChargePaid",
                        "SalaryPaymentWithWithdrawalChargePaid",
                    ),
                    ("SalaryPayment", "SalaryPayment"),
                    ("BusinessPayment", "BusinessPayment"),
                    ("PromotionPayment", "PromotionPayment"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bank",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Failed", "Failed"),
                    ("NotSupported", "NotSupported"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="btresponseentry",
            name="status",
            field=models.CharField(
                choices=[
                    ("Failed", "Failed"),
                    ("NotSupported", "NotSupported"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="businesstobusiness",
            name="provider",
            field=models.CharField(
                choices=[
                    ("TigoTanzania", "TigoTanzania"),
                    ("Mpesa", "Mpesa"),
                    ("Athena", "Athena"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="businesstobusiness",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Failed", "Failed"),
                    ("NotSupported", "NotSupported"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                ],
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="cardcheckout",
            name="status",
            field=models.CharField(
                choices=[
                    ("NotSupported", "NotSupported"),
                    ("Failed", "Failed"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("Success", "Success"),
                    ("PendingConfirmation", "PendingConfirmation"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="customertobusiness",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("InvalidRequest", "InvalidRequest"),
                    ("NotSupported", "NotSupported"),
                    ("PendingConfirmation", "PendingConfirmation"),
                    ("Failed", "Failed"),
                ],
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="topupstash",
            name="status",
            field=models.CharField(
                choices=[("Success", "Success"), ("Failed", "Failed")], max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="wallettransfer",
            name="status",
            field=models.CharField(
                choices=[("Success", "Success"), ("Failed", "Failed")], max_length=50
            ),
        ),
    ]
