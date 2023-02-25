from django.db import models
from django.contrib.gis.db import models as geo_mod

from core_delivery.basemodel import BaseModel
from core_delivery.users.models import DefaultUser, DeliveryMan


class Location(BaseModel):
    name = models.CharField(max_length=30, verbose_name="Что находится в этой точке")
    how_to_find = models.TextField(verbose_name="Как найти")
    point = geo_mod.PointField(verbose_name="Географическая точка")


class Order(BaseModel):
    content = models.CharField(max_length=30, verbose_name="Содержание заказа")
    description = models.TextField(verbose_name="Доп. информация")
    dispatch_point = models.ForeignKey(Location, related_name="dis_ord", on_delete=models.CASCADE, verbose_name="Точка отправки")
    delivery_point = models.ForeignKey(Location, related_name="del_ord", on_delete=models.CASCADE, verbose_name="Точка доставки")
    fragile = models.BooleanField(verbose_name="Хрупкий")
    receiver = models.ForeignKey(DefaultUser, related_name="rec_orders", on_delete=models.CASCADE, verbose_name="Получатель")
    delivery_man = models.ForeignKey(DeliveryMan, related_name="del_orders", null=True, on_delete=models.SET_NULL, verbose_name="Доставщик")
    distance = models.FloatField(verbose_name="Расстояние между точками")
    delivered = models.BooleanField(default=False, verbose_name="Доставлено")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")
    delivery_price = models.FloatField(default=0, verbose_name="Полная цена за доставку")
    payment = models.FloatField(default=0, verbose_name="Оплата доставщику")
    weight = models.FloatField(verbose_name="Вес отправления")
    dimension = models.JSONField(verbose_name="Габариты отправления")
    published = models.BooleanField(default=False, verbose_name="Опубликовано в очередь")


class Incident(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ с которым произошел инцидент")
    description = models.TextField(verbose_name="Описание инцидента")
    files = models.FileField(verbose_name="Прикрепленные файлы/фото/видео")
    employee_answer = models.TextField(verbose_name="Ответ работника принявшего инцидент")
    incident_handler = models.ForeignKey(DefaultUser, on_delete=models.DO_NOTHING,
                                         verbose_name="Кто обработал инцидент")


class DeliveryManReview(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name="Заказ")
    receiver = models.ForeignKey(DefaultUser, null=True, on_delete=models.SET_NULL, verbose_name="Получатель")
    deliveryman = models.ForeignKey(DeliveryMan, null=True, on_delete=models.SET_NULL, verbose_name="Доставщик")
    text = models.TextField(verbose_name="Комментарий получателя", default="")
    evaluation = models.PositiveSmallIntegerField(verbose_name="Оценка")


class ReceiverReview(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name="Заказ")
    receiver = models.ForeignKey(DefaultUser, null=True, on_delete=models.SET_NULL, verbose_name="Получатель")
    deliveryman = models.ForeignKey(DeliveryMan, null=True, on_delete=models.SET_NULL, verbose_name="Доставщик")
    text = models.TextField(verbose_name="Комментарий доставщика", default="")
    evaluation = models.PositiveSmallIntegerField(verbose_name="Оценка")


class HistoricalOrderRecord(BaseModel):
    start_time = models.TimeField(verbose_name="Старт доставки")
    end_time = models.TimeField(verbose_name="Конец доставки")
    receiving_time = models.TimeField(verbose_name="Время получения заказа доставщиком")
    incident = models.ForeignKey(Incident, null=True, on_delete=models.SET_NULL, verbose_name="Инцидент")
    log_id = models.UUIDField(verbose_name="UUID лога перемещения доставщика")
