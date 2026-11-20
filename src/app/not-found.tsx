import Link from 'next/link';
import { Button } from '@/components/ui/button';

export default function NotFound() {
  return (
    <div className="flex min-h-[60vh] flex-col items-center justify-center p-6 text-center">
      <h2 className="font-heading text-xl font-bold tracking-tight">Page Not Found</h2>
      <p className="mt-2 text-sm text-muted-foreground">
        Could not find requested resource.
      </p>
      <Button asChild className="mt-4">
        <Link href="/">
          Return Home
        </Link>
      </Button>
    </div>
  );
}
