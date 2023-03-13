from dataclasses import dataclass
from typing import Optional, Any, Dict, List, TypeVar, Callable, Type, cast
from datetime import datetime
from uuid import UUID
import dateutil.parser


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    #assert False


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Availability:
    seats: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Availability':
        assert isinstance(obj, dict)
        seats = from_union([from_int, from_none], obj.get("seats"))
        return Availability(seats)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.seats is not None:
            result["seats"] = from_union([from_int, from_none], self.seats)
        return result


@dataclass
class Conversion:
    eur: Optional[float] = None
    huf: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Conversion':
        assert isinstance(obj, dict)
        eur = from_union([from_float, from_none], obj.get("EUR"))
        huf = from_union([from_float, from_none], obj.get("HUF"))
        return Conversion(eur, huf)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.eur is not None:
            result["EUR"] = from_union([to_float, from_none], self.eur)
        if self.huf is not None:
            result["HUF"] = from_union([to_float, from_none], self.huf)
        return result


@dataclass
class Country:
    code: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Country':
        assert isinstance(obj, dict)
        code = from_union([from_str, from_none], obj.get("code"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Country(code, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.code is not None:
            result["code"] = from_union([from_str, from_none], self.code)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Duration:
    departure: Optional[int] = None
    duration_return: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Duration':
        assert isinstance(obj, dict)
        departure = from_union([from_int, from_none], obj.get("departure"))
        duration_return = from_union([from_int, from_none], obj.get("return"))
        total = from_union([from_int, from_none], obj.get("total"))
        return Duration(departure, duration_return, total)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.departure is not None:
            result["departure"] = from_union([from_int, from_none], self.departure)
        if self.duration_return is not None:
            result["return"] = from_union([from_int, from_none], self.duration_return)
        if self.total is not None:
            result["total"] = from_union([from_int, from_none], self.total)
        return result


@dataclass
class Seats:
    adults: Optional[float] = None
    children: Optional[float] = None
    infants: Optional[float] = None
    passengers: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Seats':
        assert isinstance(obj, dict)
        adults = from_union([from_float, from_none], obj.get("adults"))
        children = from_union([from_float, from_none], obj.get("children"))
        infants = from_union([from_float, from_none], obj.get("infants"))
        passengers = from_union([from_int, from_none], obj.get("passengers"))
        return Seats(adults, children, infants, passengers)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.adults is not None:
            result["adults"] = from_union([to_float, from_none], self.adults)
        if self.children is not None:
            result["children"] = from_union([to_float, from_none], self.children)
        if self.infants is not None:
            result["infants"] = from_union([to_float, from_none], self.infants)
        if self.passengers is not None:
            result["passengers"] = from_union([from_int, from_none], self.passengers)
        return result


@dataclass
class Route:
    equipment: None
    id: Optional[str] = None
    combination_id: Optional[str] = None
    fly_from: Optional[str] = None
    fly_to: Optional[str] = None
    city_from: Optional[str] = None
    city_code_from: Optional[str] = None
    city_to: Optional[str] = None
    city_code_to: Optional[str] = None
    airline: Optional[str] = None
    flight_no: Optional[int] = None
    operating_carrier: Optional[str] = None
    operating_flight_no: Optional[str] = None
    fare_basis: Optional[str] = None
    fare_category: Optional[str] = None
    fare_classes: Optional[str] = None
    fare_family: Optional[str] = None
    route_return: Optional[int] = None
    bags_recheck_required: Optional[bool] = None
    vi_connection: Optional[bool] = None
    guarantee: Optional[bool] = None
    vehicle_type: Optional[str] = None
    local_arrival: Optional[datetime] = None
    utc_arrival: Optional[datetime] = None
    local_departure: Optional[datetime] = None
    utc_departure: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Route':
        assert isinstance(obj, dict)
        equipment = from_none(obj.get("equipment"))
        id = from_union([from_str, from_none], obj.get("id"))
        combination_id = from_union([from_str, from_none], obj.get("combination_id"))
        fly_from = from_union([from_str, from_none], obj.get("flyFrom"))
        fly_to = from_union([from_str, from_none], obj.get("flyTo"))
        city_from = from_union([from_str, from_none], obj.get("cityFrom"))
        city_code_from = from_union([from_str, from_none], obj.get("cityCodeFrom"))
        city_to = from_union([from_str, from_none], obj.get("cityTo"))
        city_code_to = from_union([from_str, from_none], obj.get("cityCodeTo"))
        airline = from_union([from_str, from_none], obj.get("airline"))
        flight_no = from_union([from_int, from_none], obj.get("flight_no"))
        operating_carrier = from_union([from_str, from_none], obj.get("operating_carrier"))
        operating_flight_no = from_union([from_str, from_none], obj.get("operating_flight_no"))
        fare_basis = from_union([from_str, from_none], obj.get("fare_basis"))
        fare_category = from_union([from_str, from_none], obj.get("fare_category"))
        fare_classes = from_union([from_str, from_none], obj.get("fare_classes"))
        fare_family = from_union([from_str, from_none], obj.get("fare_family"))
        route_return = from_union([from_int, from_none], obj.get("return"))
        bags_recheck_required = from_union([from_bool, from_none], obj.get("bags_recheck_required"))
        vi_connection = from_union([from_bool, from_none], obj.get("vi_connection"))
        guarantee = from_union([from_bool, from_none], obj.get("guarantee"))
        vehicle_type = from_union([from_str, from_none], obj.get("vehicle_type"))
        local_arrival = from_union([from_datetime, from_none], obj.get("local_arrival"))
        utc_arrival = from_union([from_datetime, from_none], obj.get("utc_arrival"))
        local_departure = from_union([from_datetime, from_none], obj.get("local_departure"))
        utc_departure = from_union([from_datetime, from_none], obj.get("utc_departure"))
        return Route(equipment, id, combination_id, fly_from, fly_to, city_from, city_code_from, city_to, city_code_to, airline, flight_no, operating_carrier, operating_flight_no, fare_basis, fare_category, fare_classes, fare_family, route_return, bags_recheck_required, vi_connection, guarantee, vehicle_type, local_arrival, utc_arrival, local_departure, utc_departure)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.equipment is not None:
            result["equipment"] = from_none(self.equipment)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.combination_id is not None:
            result["combination_id"] = from_union([from_str, from_none], self.combination_id)
        if self.fly_from is not None:
            result["flyFrom"] = from_union([from_str, from_none], self.fly_from)
        if self.fly_to is not None:
            result["flyTo"] = from_union([from_str, from_none], self.fly_to)
        if self.city_from is not None:
            result["cityFrom"] = from_union([from_str, from_none], self.city_from)
        if self.city_code_from is not None:
            result["cityCodeFrom"] = from_union([from_str, from_none], self.city_code_from)
        if self.city_to is not None:
            result["cityTo"] = from_union([from_str, from_none], self.city_to)
        if self.city_code_to is not None:
            result["cityCodeTo"] = from_union([from_str, from_none], self.city_code_to)
        if self.airline is not None:
            result["airline"] = from_union([from_str, from_none], self.airline)
        if self.flight_no is not None:
            result["flight_no"] = from_union([from_int, from_none], self.flight_no)
        if self.operating_carrier is not None:
            result["operating_carrier"] = from_union([from_str, from_none], self.operating_carrier)
        if self.operating_flight_no is not None:
            result["operating_flight_no"] = from_union([from_str, from_none], self.operating_flight_no)
        if self.fare_basis is not None:
            result["fare_basis"] = from_union([from_str, from_none], self.fare_basis)
        if self.fare_category is not None:
            result["fare_category"] = from_union([from_str, from_none], self.fare_category)
        if self.fare_classes is not None:
            result["fare_classes"] = from_union([from_str, from_none], self.fare_classes)
        if self.fare_family is not None:
            result["fare_family"] = from_union([from_str, from_none], self.fare_family)
        if self.route_return is not None:
            result["return"] = from_union([from_int, from_none], self.route_return)
        if self.bags_recheck_required is not None:
            result["bags_recheck_required"] = from_union([from_bool, from_none], self.bags_recheck_required)
        if self.vi_connection is not None:
            result["vi_connection"] = from_union([from_bool, from_none], self.vi_connection)
        if self.guarantee is not None:
            result["guarantee"] = from_union([from_bool, from_none], self.guarantee)
        if self.vehicle_type is not None:
            result["vehicle_type"] = from_union([from_str, from_none], self.vehicle_type)
        if self.local_arrival is not None:
            result["local_arrival"] = from_union([lambda x: x.isoformat(), from_none], self.local_arrival)
        if self.utc_arrival is not None:
            result["utc_arrival"] = from_union([lambda x: x.isoformat(), from_none], self.utc_arrival)
        if self.local_departure is not None:
            result["local_departure"] = from_union([lambda x: x.isoformat(), from_none], self.local_departure)
        if self.utc_departure is not None:
            result["utc_departure"] = from_union([lambda x: x.isoformat(), from_none], self.utc_departure)
        return result


@dataclass
class Datum:
    id: Optional[str] = None
    fly_from: Optional[str] = None
    fly_to: Optional[str] = None
    city_from: Optional[str] = None
    city_code_from: Optional[str] = None
    city_to: Optional[str] = None
    city_code_to: Optional[str] = None
    country_from: Optional[Country] = None
    country_to: Optional[Country] = None
    nights_in_dest: Optional[int] = None
    quality: Optional[float] = None
    distance: Optional[float] = None
    duration: Optional[Duration] = None
    price: Optional[float] = None
    conversion: Optional[Conversion] = None
    fare: Optional[Seats] = None
    bags_price: Optional[Dict[str, float]] = None
    baglimit: Optional[Dict[str, int]] = None
    availability: Optional[Availability] = None
    airlines: Optional[List[str]] = None
    route: Optional[List[Route]] = None
    booking_token: Optional[str] = None
    deep_link: Optional[str] = None
    facilitated_booking_available: Optional[bool] = None
    pnr_count: Optional[int] = None
    has_airport_change: Optional[bool] = None
    technical_stops: Optional[int] = None
    throw_away_ticketing: Optional[bool] = None
    hidden_city_ticketing: Optional[bool] = None
    virtual_interlining: Optional[bool] = None
    local_arrival: Optional[datetime] = None
    utc_arrival: Optional[datetime] = None
    local_departure: Optional[datetime] = None
    utc_departure: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        fly_from = from_union([from_str, from_none], obj.get("flyFrom"))
        fly_to = from_union([from_str, from_none], obj.get("flyTo"))
        city_from = from_union([from_str, from_none], obj.get("cityFrom"))
        city_code_from = from_union([from_str, from_none], obj.get("cityCodeFrom"))
        city_to = from_union([from_str, from_none], obj.get("cityTo"))
        city_code_to = from_union([from_str, from_none], obj.get("cityCodeTo"))
        country_from = from_union([Country.from_dict, from_none], obj.get("countryFrom"))
        country_to = from_union([Country.from_dict, from_none], obj.get("countryTo"))
        nights_in_dest = from_union([from_int, from_none], obj.get("nightsInDest"))
        quality = from_union([from_float, from_none], obj.get("quality"))
        distance = from_union([from_float, from_none], obj.get("distance"))
        duration = from_union([Duration.from_dict, from_none], obj.get("duration"))
        price = from_union([from_float, from_none], obj.get("price"))
        conversion = from_union([Conversion.from_dict, from_none], obj.get("conversion"))
        fare = from_union([Seats.from_dict, from_none], obj.get("fare"))
        bags_price = from_union([lambda x: from_dict(from_float, x), from_none], obj.get("bags_price"))
        baglimit = from_union([lambda x: from_dict(from_int, x), from_none], obj.get("baglimit"))
        availability = from_union([Availability.from_dict, from_none], obj.get("availability"))
        airlines = from_union([lambda x: from_list(from_str, x), from_none], obj.get("airlines"))
        route = from_union([lambda x: from_list(Route.from_dict, x), from_none], obj.get("route"))
        booking_token = from_union([from_str, from_none], obj.get("booking_token"))
        deep_link = from_union([from_str, from_none], obj.get("deep_link"))
        facilitated_booking_available = from_union([from_bool, from_none], obj.get("facilitated_booking_available"))
        pnr_count = from_union([from_int, from_none], obj.get("pnr_count"))
        has_airport_change = from_union([from_bool, from_none], obj.get("has_airport_change"))
        technical_stops = from_union([from_int, from_none], obj.get("technical_stops"))
        throw_away_ticketing = from_union([from_bool, from_none], obj.get("throw_away_ticketing"))
        hidden_city_ticketing = from_union([from_bool, from_none], obj.get("hidden_city_ticketing"))
        virtual_interlining = from_union([from_bool, from_none], obj.get("virtual_interlining"))
        local_arrival = from_union([from_datetime, from_none], obj.get("local_arrival"))
        utc_arrival = from_union([from_datetime, from_none], obj.get("utc_arrival"))
        local_departure = from_union([from_datetime, from_none], obj.get("local_departure"))
        utc_departure = from_union([from_datetime, from_none], obj.get("utc_departure"))
        return Datum(id, fly_from, fly_to, city_from, city_code_from, city_to, city_code_to, country_from, country_to, nights_in_dest, quality, distance, duration, price, conversion, fare, bags_price, baglimit, availability, airlines, route, booking_token, deep_link, facilitated_booking_available, pnr_count, has_airport_change, technical_stops, throw_away_ticketing, hidden_city_ticketing, virtual_interlining, local_arrival, utc_arrival, local_departure, utc_departure)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.fly_from is not None:
            result["flyFrom"] = from_union([from_str, from_none], self.fly_from)
        if self.fly_to is not None:
            result["flyTo"] = from_union([from_str, from_none], self.fly_to)
        if self.city_from is not None:
            result["cityFrom"] = from_union([from_str, from_none], self.city_from)
        if self.city_code_from is not None:
            result["cityCodeFrom"] = from_union([from_str, from_none], self.city_code_from)
        if self.city_to is not None:
            result["cityTo"] = from_union([from_str, from_none], self.city_to)
        if self.city_code_to is not None:
            result["cityCodeTo"] = from_union([from_str, from_none], self.city_code_to)
        if self.country_from is not None:
            result["countryFrom"] = from_union([lambda x: to_class(Country, x), from_none], self.country_from)
        if self.country_to is not None:
            result["countryTo"] = from_union([lambda x: to_class(Country, x), from_none], self.country_to)
        if self.nights_in_dest is not None:
            result["nightsInDest"] = from_union([from_int, from_none], self.nights_in_dest)
        if self.quality is not None:
            result["quality"] = from_union([to_float, from_none], self.quality)
        if self.distance is not None:
            result["distance"] = from_union([to_float, from_none], self.distance)
        if self.duration is not None:
            result["duration"] = from_union([lambda x: to_class(Duration, x), from_none], self.duration)
        if self.price is not None:
            result["price"] = from_union([to_float, from_none], self.price)
        if self.conversion is not None:
            result["conversion"] = from_union([lambda x: to_class(Conversion, x), from_none], self.conversion)
        if self.fare is not None:
            result["fare"] = from_union([lambda x: to_class(Seats, x), from_none], self.fare)
        if self.bags_price is not None:
            result["bags_price"] = from_union([lambda x: from_dict(to_float, x), from_none], self.bags_price)
        if self.baglimit is not None:
            result["baglimit"] = from_union([lambda x: from_dict(from_int, x), from_none], self.baglimit)
        if self.availability is not None:
            result["availability"] = from_union([lambda x: to_class(Availability, x), from_none], self.availability)
        if self.airlines is not None:
            result["airlines"] = from_union([lambda x: from_list(from_str, x), from_none], self.airlines)
        if self.route is not None:
            result["route"] = from_union([lambda x: from_list(lambda x: to_class(Route, x), x), from_none], self.route)
        if self.booking_token is not None:
            result["booking_token"] = from_union([from_str, from_none], self.booking_token)
        if self.deep_link is not None:
            result["deep_link"] = from_union([from_str, from_none], self.deep_link)
        if self.facilitated_booking_available is not None:
            result["facilitated_booking_available"] = from_union([from_bool, from_none], self.facilitated_booking_available)
        if self.pnr_count is not None:
            result["pnr_count"] = from_union([from_int, from_none], self.pnr_count)
        if self.has_airport_change is not None:
            result["has_airport_change"] = from_union([from_bool, from_none], self.has_airport_change)
        if self.technical_stops is not None:
            result["technical_stops"] = from_union([from_int, from_none], self.technical_stops)
        if self.throw_away_ticketing is not None:
            result["throw_away_ticketing"] = from_union([from_bool, from_none], self.throw_away_ticketing)
        if self.hidden_city_ticketing is not None:
            result["hidden_city_ticketing"] = from_union([from_bool, from_none], self.hidden_city_ticketing)
        if self.virtual_interlining is not None:
            result["virtual_interlining"] = from_union([from_bool, from_none], self.virtual_interlining)
        if self.local_arrival is not None:
            result["local_arrival"] = from_union([lambda x: x.isoformat(), from_none], self.local_arrival)
        if self.utc_arrival is not None:
            result["utc_arrival"] = from_union([lambda x: x.isoformat(), from_none], self.utc_arrival)
        if self.local_departure is not None:
            result["local_departure"] = from_union([lambda x: x.isoformat(), from_none], self.local_departure)
        if self.utc_departure is not None:
            result["utc_departure"] = from_union([lambda x: x.isoformat(), from_none], self.utc_departure)
        return result


@dataclass
class SearchParams:
    fly_from_type: Optional[str] = None
    to_type: Optional[str] = None
    seats: Optional[Seats] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SearchParams':
        assert isinstance(obj, dict)
        fly_from_type = from_union([from_str, from_none], obj.get("flyFrom_type"))
        to_type = from_union([from_str, from_none], obj.get("to_type"))
        seats = from_union([Seats.from_dict, from_none], obj.get("seats"))
        return SearchParams(fly_from_type, to_type, seats)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.fly_from_type is not None:
            result["flyFrom_type"] = from_union([from_str, from_none], self.fly_from_type)
        if self.to_type is not None:
            result["to_type"] = from_union([from_str, from_none], self.to_type)
        if self.seats is not None:
            result["seats"] = from_union([lambda x: to_class(Seats, x), from_none], self.seats)
        return result


@dataclass
class FlightResultModel:
    search_id: Optional[UUID] = None
    currency: Optional[str] = None
    fx_rate: Optional[float] = None
    data: Optional[List[Datum]] = None
    results: Optional[int] = None
    search_params: Optional[SearchParams] = None
    all_stopover_airports: Optional[List[Any]] = None
    sort_version: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FlightResultModel':
        assert isinstance(obj, dict)
        search_id = from_union([lambda x: UUID(x), from_none], obj.get("search_id"))
        currency = from_union([from_str, from_none], obj.get("currency"))
        fx_rate = from_union([from_float, from_none], obj.get("fx_rate"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        results = from_union([from_int, from_none], obj.get("_results"))
        search_params = from_union([SearchParams.from_dict, from_none], obj.get("search_params"))
        all_stopover_airports = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("all_stopover_airports"))
        sort_version = from_union([from_int, from_none], obj.get("sort_version"))
        return FlightResultModel(search_id, currency, fx_rate, data, results, search_params, all_stopover_airports, sort_version)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.search_id is not None:
            result["search_id"] = from_union([lambda x: str(x), from_none], self.search_id)
        if self.currency is not None:
            result["currency"] = from_union([from_str, from_none], self.currency)
        if self.fx_rate is not None:
            result["fx_rate"] = from_union([to_float, from_none], self.fx_rate)
        if self.data is not None:
            result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        if self.results is not None:
            result["_results"] = from_union([from_int, from_none], self.results)
        if self.search_params is not None:
            result["search_params"] = from_union([lambda x: to_class(SearchParams, x), from_none], self.search_params)
        if self.all_stopover_airports is not None:
            result["all_stopover_airports"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.all_stopover_airports)
        if self.sort_version is not None:
            result["sort_version"] = from_union([from_int, from_none], self.sort_version)
        return result


def flight_result_model_from_dict(s: Any) -> FlightResultModel:
    return FlightResultModel.from_dict(s)


def flight_result_model_to_dict(x: FlightResultModel) -> Any:
    return to_class(FlightResultModel, x)
