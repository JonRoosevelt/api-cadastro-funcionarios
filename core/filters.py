import datetime

from django_filters import rest_framework as filters

from .models import Naver


class NaversIndexFilter(filters.FilterSet):
    def init(self, queryset, name, value):
        try:
            initial, end = value.split(',')
        except ValueError:
            end = value
            initial = 0
        self.initial = int(initial)
        self.end = int(end)
        self.queryset = queryset
        self.filter_type = name.split('_')[-1]

    company_time_in_years = filters.CharFilter(method='filter_company_time')
    company_time_in_months = filters.CharFilter(method='filter_company_time')
    company_time_in_days = filters.CharFilter(method='filter_company_time')

    def get_time_in_days(self, admission_date):
        today = datetime.date.today()
        return (
            ((today.year - admission_date.year) * 12
             + today.month - admission_date.month) * 30
        )

    def get_time_in_months(self, admission_date):
        today = datetime.date.today()
        return (
            (today.year - admission_date.year) * 12
            + today.month - admission_date.month
        )

    def get_time_in_years(self, admission_date):
        today = datetime.date.today()
        if today.month < admission_date.month or (
                today.month == admission_date.month and
                today.day < admission_date.day):
            return today.year - admission_date.year - 1
        else:
            return today.year - admission_date.year

    def get_company_time(self, admission_date):
        times_types = dict(
            days=self.get_time_in_days,
            months=self.get_time_in_months,
            years=self.get_time_in_years,
        )
        return times_types[self.filter_type](admission_date)

    def get_company_time_tuple(self, naver):
        return (
            self.get_company_time(naver.admission_date),
            dict(
                admission_date=naver.admission_date,
                naver_id=naver.id
            )
        )

    def sort_list(self, company_times):
        return sorted(
            company_times, key=lambda x: x[0])

    def is_in_range(self, tuple):
        return tuple[0] >= self.initial and tuple[0] <= self.end

    def get_filtered_company_times(
            self, sorted_company_times):
        return [c for c in sorted_company_times
                if self.is_in_range(c)]

    def filter_company_time(self, queryset, name, value):
        self.init(queryset, name, value)

        if self.initial >= 0 and self.end >= 0:
            company_times = [self.get_company_time_tuple(
                naver) for naver in self.queryset]
            sorted_company_times = self.sort_list(company_times)
            filtered_company_times = self.get_filtered_company_times(
                sorted_company_times)
            return (
                self.queryset
                .filter(
                    id__in=[c[1]['naver_id']
                            for c in filtered_company_times]
                )
            )
        return self.queryset

    class Meta:
        model = Naver
        fields = ('__all__')
