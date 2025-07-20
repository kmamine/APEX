import { ReactNode } from 'react';
import { cn } from '../../utils';

interface CardProps {
  children: ReactNode;
  className?: string;
  title?: string;
  description?: string;
}

export const Card = ({ children, className, title, description }: CardProps) => {
  return (
    <div className={cn('card', className)}>
      {title && (
        <div className="mb-4">
          <h3 className="section-title">{title}</h3>
          {description && (
            <p className="text-gray-600 text-sm">{description}</p>
          )}
        </div>
      )}
      {children}
    </div>
  );
};
