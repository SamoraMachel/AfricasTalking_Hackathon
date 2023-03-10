# Generated by Django 4.1.5 on 2023-02-03 04:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "aft_payment",
            "0002_alter_b2centries_status_alter_b2crecipient_reason_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="b2centries",
            name="status",
            field=models.CharField(
                choices=[
                    ("Failed", "Failed"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                    ("NotSupported", "NotSupported"),
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
                    ("PromotionPayment", "PromotionPayment"),
                    ("SalaryPayment", "SalaryPayment"),
                    ("BusinessPayment", "BusinessPayment"),
                    (
                        "SalaryPaymentWithWithdrawalChargePaid",
                        "SalaryPaymentWithWithdrawalChargePaid",
                    ),
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
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                    ("NotSupported", "NotSupported"),
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
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                    ("NotSupported", "NotSupported"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="businesstobusiness",
            name="provider",
            field=models.CharField(
                choices=[
                    ("Athena", "Athena"),
                    ("Mpesa", "Mpesa"),
                    ("TigoTanzania", "TigoTanzania"),
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
                    ("InvalidRequest", "InvalidRequest"),
                    ("Queued", "Queued"),
                    ("NotSupported", "NotSupported"),
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
                    ("Success", "Success"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("PendingConfirmation", "PendingConfirmation"),
                    ("Failed", "Failed"),
                    ("NotSupported", "NotSupported"),
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
                    ("Failed", "Failed"),
                    ("InvalidRequest", "InvalidRequest"),
                    ("NotSupported", "NotSupported"),
                    ("PendingConfirmation", "PendingConfirmation"),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]
