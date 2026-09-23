#!/usr/bin/env python3

from app import create_app
from app.models import Plant
from app.db import db

app=create_app()
with app.app_context():

    Plant.query.delete()

    aloe = Plant(
        name="Aloe",
        image="/images/aloe.jpg",
        price=11.50,
    )

    zz_plant = Plant(
        name="ZZ Plant",
        image="/images/zz-plant.jpg",
        price=25.98,
    )
    calathea = Plant(
        name="Calathea",
        image="/images/calathea.jpg",
        price=30.00,
    )
    jade = Plant(
        name="Jade",
        image="/images/jade.jpg",
        price=22.67,
    )
    fiddle = Plant(
        name="Fiddle-leaf",
        image="/images/fiddle-leaf.jpg",
        price=40.67,
    )
    monstera = Plant(
        name="Monstera ",
        image="/images/monstera.jpg",
        price=25.98,
    )
    pilea = Plant(
        name="Pilea",
        image="/images/pilea.jpg",
        price=25.98,
    )
    pothos = Plant(
        name="Pothos",
        image="/images/pothos.jpg",
        price=25.98,
    )

    plants=[aloe,calathea,fiddle,jade,monstera,pilea,pothos,zz_plant]
    db.session.add_all(plants)
    db.session.commit()