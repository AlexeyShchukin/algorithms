-- У компании по доставке еды есть таблица deliveries заказов пеших курьеров.
-- В конце каждого месяца компания выдает премию для своих курьеров,
-- средняя скорость доставки за прошедший месяц которых больше средней скорости среди всех курьеров.
-- Необходимо узнать сколько курьеров получили премию за июль 2024.

-- Важно! Средняя скорость рассчитывается как суммарное расстояние за период делить на суммарное время доставок.

-- Поле в результирующей таблице: rewarded_couriers

-- Fields: date	 courier_id	 order_id	distance	travel_time

with speed as (select
                    courier_id,
                    sum(distance) / sum(travel_time) as avg_speed
               from deliveries
               where date between '2024-07-01' and '2024-07-31'
               group by courier_id)

select count(courier_id) as rewarded_couriers
from speed
where avg_speed > (select avg(avg_speed) from speed)
