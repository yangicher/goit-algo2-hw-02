from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    printer = PrinterConstraints(**constraints)

    jobs.sort(key=lambda j: j.priority)

    total_time = 0
    print_order = []

    i = 0
    while i < len(jobs):
        current_group = []
        current_volume = 0

        while (
            i < len(jobs)
            and len(current_group) < printer.max_items
            and current_volume + jobs[i].volume <= printer.max_volume
        ):
            current_group.append(jobs[i])
            current_volume += jobs[i].volume
            i += 1

        if current_group:
            group_time = max(job.print_time for job in current_group)
            total_time += group_time
            print_order.extend(job.id for job in current_group)
        else:
            job = jobs[i]
            total_time += job.print_time
            print_order.append(job.id)
            i += 1

    return {"print_order": print_order, "total_time": total_time}


def test_printing_optimization():
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {"max_volume": 300, "max_items": 2}

    print("Тест 1 (однаковий пріоритет):")
    r1 = optimize_printing(test1_jobs, constraints)
    print(r1)

    print("\nТест 2 (різні пріоритети):")
    r2 = optimize_printing(test2_jobs, constraints)
    print(r2)

    print("\nТест 3 (перевищення обмежень):")
    r3 = optimize_printing(test3_jobs, constraints)
    print(r3)

if __name__ == "__main__":
    test_printing_optimization()